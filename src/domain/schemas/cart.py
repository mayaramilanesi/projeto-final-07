from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field

from src.domain.schemas.user import UserSchema


class CartSchema(BaseModel):
    user: UserSchema
    products: list[]
    total_price: Decimal = Field(max_digits=10, decimal_places=2)
    opened: bool = Field(default=True)
    