from decimal import Decimal
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field
from src.domain.schemas.product import ProductSchema
from src.domain.schemas.user import UserSchema

class CartSchema(BaseModel):
    user_email = str
    products: List=[]
    total_price: Decimal = Field(default=0.0)
    opened: bool = Field(default=True)
    