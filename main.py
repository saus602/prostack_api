from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
import models, schemas

# Initialize FastAPI
app = FastAPI()

# Create database tables if they don’t exist
Base.metadata.create_all(bind=engine)


# ---------- Health Check ----------
@app.get("/")
def read_root():
    return {"message": "🚀 ProStack API is running!"}

@app.get("/health")
def health():
    return {"status": "ok"}


# ---------- Cards Endpoints ----------
@app.get("/cards", response_model=list[schemas.Card])
def read_cards(db: Session = Depends(get_db)):
    try:
        cards = db.query(models.Card).all()
        return cards
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@app.post("/cards", response_model=schemas.Card)
def create_card(card: schemas.CardCreate, db: Session = Depends(get_db)):
    try:
        db_card = models.Card(**card.dict())
        db.add(db_card)
        db.commit()
        db.refresh(db_card)
        return db_card
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create card: {str(e)}")
