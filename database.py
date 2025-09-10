import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Pull DATABASE_URL from environment variable (Railway sets this automatically)
# Fallback is for local testing
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:prostack_pass@localhost:5432/prostackdb"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
