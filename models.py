from sqlalchemy import Column, Integer, String, Boolean, Numeric, Text
from database import Base

class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    bank_name = Column(String(100), nullable=False)
    card_name = Column(String(100), nullable=False)
    type = Column(String(20), nullable=False)  # "personal" or "business"
    est_limit_min = Column(Integer, nullable=False)
    est_limit_max = Column(Integer, nullable=False)
    approval_pct = Column(Numeric(5, 2), nullable=False)
    instant_approval = Column(Boolean, default=False)
    application_url = Column(Text, nullable=False)
    notes = Column(Text, nullable=True)
