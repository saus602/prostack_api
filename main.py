# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models, schemas
from database import engine, Base, get_db

# Create all database tables (if they don't exist yet)
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="ProStack API", version="1.0.0")


# ------------------------
# ROUTES
# ------------------------

# Get all cards
@app.get("/cards", response_model=list[schemas.Card])
def read_cards(db: Session = Depends(get_db)):
    cards = db.query(models.Card).all()
    return cards


# Get a single card by ID
@app.get("/cards/{card_id}", response_model=schemas.Card)
def read_card(card_id: int, db: Session = Depends(get_db)):
    card = db.query(models.Card).filter(models.Card.id == card_id).first()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    return card


# Add a new card
@app.post("/cards", response_model=schemas.Card)
def create_card(card: schemas.CardCreate, db: Session = Depends(get_db)):
    db_card = models.Card(**card.dict())
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card


# Delete a card
@app.delete("/cards/{card_id}")
def delete_card(card_id: int, db: Session = Depends(get_db)):
    card = db.query(models.Card).filter(models.Card.id == card_id).first()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    db.delete(card)
    db.commit()
    return {"detail": "Card deleted successfully"}
