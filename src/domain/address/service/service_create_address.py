from src.domain.schemas.address import AddressSchema
from src.domain.address.models.get_address_by_email import get_address_by_email
from src.domain.address.models.create_new_address import create_new_address
from src.domain.address.models.create_address import create_address



async def service_create_address(address: AddressSchema, email):

      address_dict = address.dict()
      address_user = await get_address_by_email(email)

      if not address_user:
            result = await create_new_address(address_dict)
            return result
      else:
            result = await create_address(address_dict)
            return result
