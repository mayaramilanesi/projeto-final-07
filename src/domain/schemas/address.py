from typing import List
from pydantic import BaseModel, EmailStr, Field
from bson.objectid import ObjectId



class Address(BaseModel):
    _id: ObjectId()
    street: str
    number: int
    complement: str
    district: str
    zip_code: str
    city: str
    state: str
    is_delivery: bool = Field(default=True)


class AddressSchema(BaseModel):
    user: EmailStr
    address: List[Address]
    
class EmailSchema(BaseModel):
    email: str
    
