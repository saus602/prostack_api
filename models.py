# models.py
from sqlalchemy import Column, Integer, String, Boolean, Float
from database import Base

class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    bank_name = Column(String, nullable=False)
    card_name = Column(String, nullable=False)
    type = Column(String, nullable=False)   # e.g., Personal, Business
    est_limit_min = Column(Float, nullable=True)
    est_limit_max = Column(Float, nullable=True)
    approval_pct = Column(Float, nullable=True)
    instant_approval = Column(Boolean, default=False)
    application_url = Column(String, nullable=True)
    notes = Column(String, nullable=True)
