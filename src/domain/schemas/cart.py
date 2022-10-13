from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field

class CartSchema(BaseModel):
    user_email = str
    products: List=[]
    total_price: Decimal = Field(default=0.0)
    total_quantity: int
    opened: bool = Field(default=True)
    
    