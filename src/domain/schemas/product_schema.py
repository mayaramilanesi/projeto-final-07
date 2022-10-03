from pydantic import BaseModel, Field 
from typing import Optional


class ProductSchema(BaseModel):
    name: str = Field(
        unique=True, 
        max_length=100)
    
    description: str
    price: float= Field(
        min=0.01)
    image: str
    code: str 
    category: str
    inventory: int=Field(
        min=1)
    
    Field(unique=True)
    
class ProductUpdatedSchema(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    image: Optional[str]
    category: Optional[str]
    inventory: Optional[int]
    code: str

    