from typing import List
from pydantic import BaseModel, Field
from bson.objectid import ObjectId

from src.domain.schemas import ClientSchema


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
    user: ClientSchema["_Id"]
    address: List[Address] = []
    
