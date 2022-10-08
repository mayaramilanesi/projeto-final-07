from src.domain.address.models.model_get_all_address import get_all_address
from src.util.service import format_json

async def service_find_all_address():
      return format_json(await get_all_address())
            

            
