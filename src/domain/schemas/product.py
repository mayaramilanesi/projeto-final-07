from pydantic import BaseModel, Field, conint, condecimal
from typing import Optional


class ProductSchema(BaseModel):
    name: str = Field(
        unique=True)
    
    description: str
    price: condecimal(ge=0.01,
    decimal_places=2)
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
    code: str

    