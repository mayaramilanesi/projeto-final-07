from decimal import Decimal
from email.policy import default
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field


from src.domain.schemas.user import UserSchema


class CartSchema(BaseModel):
    user: EmailStr
    products: Field(default=[])
    total_price: Decimal = Field(default=0.0)
    opened: bool = Field(default=True)
    