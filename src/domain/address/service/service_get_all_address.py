from src.domain.address.models.model_get_all_address import get_all_address


async def service_find_all_address():

      result = await get_all_address()
      return result
            

            
