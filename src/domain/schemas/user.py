from pydantic import BaseModel, Field
from pydantic.networks import EmailStr


class UserSchema(BaseModel):
      name: str
      email: EmailStr = Field(unique=True)
      password: str
      cellphone : int
      birth_date: int
      cpf: int
      is_active: bool = Field(default=True)    
      is_admin: bool = Field(default=False)
      
      