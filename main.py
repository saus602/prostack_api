from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, get_db
import models, schemas

# Create tables automatically at startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ProStack API")

# ------------------------------
# Routes
# ------------------------------

@app.get("/")
def root():
    return {"message": "Welcome to ProStack API 🚀"}


# Get all cards
@app.get("/cards", response_model=list[schemas.Card])
def read_cards(db: Session = Depends(get_db)):
    return db.query(models.Card).all()


# Add new card
@app.post("/cards", response_model=schemas.Card)
def create_card(card: schemas.CardCreate, db: Session = Depends(get_db)):
    db_card = models.Card(**card.dict())
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card


# Get all clients
@app.get("/clients", response_model=list[schemas.Client])
def read_clients(db: Session = Depends(get_db)):
    return db.query(models.Client).all()


# Add new client
@app.post("/clients", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    db_client = models.Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client
