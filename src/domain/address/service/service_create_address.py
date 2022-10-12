from audioop import add
from src.domain.schemas.address import AddressSchema
from src.domain.address.models.get_address_by_email import get_address_by_email
from src.domain.address.models.create_new_address import create_new_address
from src.domain.address.models.create_address import create_address
from bson.objectid import ObjectId


async def service_create_address(address: AddressSchema):
      
      
      address_dict = address.dict()
      for x in address_dict["address"]:
            x["_id"] =  ObjectId()
      
      address_user = await get_address_by_email(address.user)

      if not address_user:
            result = await create_new_address(address_dict)
            return result
      else:
            result = await create_address(address_dict)
            return result
