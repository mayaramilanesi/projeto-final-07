from src.domain.address.models.model_get_all_address import get_all_address
import json

async def service_find_all_address():

      all_address = await get_all_address()
      if all_address == False:
            return False
      all_address_json = json.loads(all_address)
      json_formatted_srt = json.dumps(all_address_json)
      return json_formatted_srt
            

            
