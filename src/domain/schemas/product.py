from pydantic import BaseModel, Field, conint
from typing import Optional


class ProductSchema(BaseModel):
    name: str = Field(
        unique=True)
    
    description: str
    price: float
    image: str
    code: str=Field()
    category: str
    inventory: conint(ge=1)
    
class ProductUpdatedSchema(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    image: Optional[str]
    category: Optional[str]
    inventory: Optional[int]

class ProductCartSchema(BaseModel):
    name: str
    price: float
    quantity: conint(ge=1)
    code: str=Field()
    