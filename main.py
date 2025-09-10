from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import engine, Base, get_db

# Create all database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# --- Health & Root Routes ---
@app.get("/")
def read_root():
    return {"message": "Hello from Railway! 🚀"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

# --- Example Endpoints ---

@app.get("/clients", response_model=list[schemas.Client])
def get_clients(db: Session = Depends(get_db)):
    """Fetch all clients"""
    return db.query(models.Client).all()


@app.post("/clients", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    """Create a new client"""
    db_client = models.Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client
