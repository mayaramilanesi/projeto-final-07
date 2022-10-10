from src.domain.address.models.get_address_by_email import get_address_by_email

async def service_get_address_by_email(email):

      user_address = await get_address_by_email(email)
      return user_address