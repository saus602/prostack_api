# main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
import models, schemas

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI(title="ProStack API", version="1.0.0")

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the ProStack API 🚀"}

# Health check
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Create a new user
@app.post("/users/", response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Store user (⚠️ plain password for now; hash in production)
    new_user = models.User(
        email=user.email,
        hashed_password=user.password,
        full_name=user.full_name
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Get all users
@app.get("/users/", response_model=list[schemas.UserRead])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()
