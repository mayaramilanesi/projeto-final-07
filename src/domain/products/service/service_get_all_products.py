from src.domain.products.models.get_all_products import get_all_products
from src.util.service import format_json


async def service_get_all_products():
      try:
            return format_json(await get_all_products())
      except Exception as e:
                return (f'get_all_products_error {e}')

   
     

