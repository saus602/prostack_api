# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# ----------------------------
# DATABASE URL
# ----------------------------
# Example for PostgreSQL:
# postgresql://username:password@localhost:5432/prostackdb
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:prostack_pass@localhost:5432/prostackdb"
)

# Create engine
engine = create_engine(DATABASE_URL)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency for getting DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
