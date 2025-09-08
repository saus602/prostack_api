# schemas.py
from pydantic import BaseModel, ConfigDict
from typing import Optional

class CardBase(BaseModel):
    bank_name: str
    card_name: str
    type: str
    est_limit_min: Optional[float] = None
    est_limit_max: Optional[float] = None
    approval_pct: Optional[float] = None
    instant_approval: Optional[bool] = None
    application_url: Optional[str] = None
    notes: Optional[str] = None


class CardCreate(CardBase):
    pass


class Card(CardBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
