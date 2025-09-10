from pydantic import BaseModel

class CardBase(BaseModel):
    bank_name: str
    card_name: str
    type: str            # "personal" or "business"
    est_limit_min: int
    est_limit_max: int
    approval_pct: float
    instant_approval: bool
    application_url: str
    notes: str | None = None

class CardCreate(CardBase):
    pass

class Card(CardBase):
    id: int

    class Config:
        from_attributes = True   # replaces orm_mode in Pydantic v2
