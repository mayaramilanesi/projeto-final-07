from src.domain.address.models.get_all_address import get_all_address


async def service_get_all_address():

      result = await get_all_address()
      return result
            

            
