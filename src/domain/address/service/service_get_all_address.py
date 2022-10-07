from src.domain.address.models.model_get_all_address import get_all_address

async def service_find_all_address():

      all_address = await get_all_address()
      if all_address == False:
            return False
      return all_address
            

            
