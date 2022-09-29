from pydantic import BaseModel, Field
from pydantic import Optional 
from pydantic.networks import EmailStr


class ClientSchema(BaseModel):
      name: str
      email: EmailStr = Field(unique=True, index=True)
      password: str
      is_active: bool = Field(default=True)    
      is_admin: bool = Field(default=False)
      
      