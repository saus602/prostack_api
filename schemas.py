# schemas.py

from pydantic import BaseModel, EmailStr
from datetime import datetime

# Shared properties
class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None


# For creating users (password is required)
class UserCreate(UserBase):
    password: str


# For reading users (what we return to the client)
class UserRead(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # allows ORM → Pydantic conversion
