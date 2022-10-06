from src.domain.products.models.get_all_products import get_all_products
from typing import List



#Ainda não está ajustado de acordo com a arquitetura e regras que definimos
async def service_get_all_products() -> List[dict]:
    all_products = await get_all_products()
    if all_products is None:
        return {'message': 'No products were found'}
    else: 
        return all_products

