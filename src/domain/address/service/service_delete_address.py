from src.domain.schemas.address import EmailSchema
from src.domain.address.models.get_address_by_email import get_address_by_email
from src.domain.address.models.delete_address import delete_address

""" async def service_delete_address(email: EmailSchema, address_id):

      address_user = await get_address_by_email(email)
      id = address_user["_id"]

      result = await delete_address(address_id: id)
      
      return """
      