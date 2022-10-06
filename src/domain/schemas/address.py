from typing import List
from pydantic import BaseModel, Field
from bson.objectid import ObjectId



class Address(BaseModel):
    _id: ObjectId()
    street: str
    number: int
    complement: str
    district: str
    cep: str
    city: str
    state: str
    is_delivery: bool = Field(default=True)


class AddressSchema(BaseModel):
    user: str
    address: List[Address] = []
    
