from src.domain.address.models.get_address_by_email import get_address_by_email
from src.util.service import format_json


async def service_get_address_by_email(email):
      
      result = format_json(await get_address_by_email(email))
      return result
      
      
 