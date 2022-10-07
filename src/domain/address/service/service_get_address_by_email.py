from src.domain.address.models.get_address_by_email import get_address_by_email

from src.domain.schemas.address import EmailSchema

async def service_get_address_by_email(email: EmailSchema):
      
      result = await get_address_by_email(email)
      
      return result
      
      
 