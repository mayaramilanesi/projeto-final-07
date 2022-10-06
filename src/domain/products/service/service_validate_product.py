
from src.domain.products.models.get_product_by_name import get_product_by_name
from src.domain.products.models.get_product_by_code import get_product_by_code



#Validar se já existe product com o nome 
async def service_validate_product_name(product_name):
    product_searched = await get_product_by_name(product_name)
    if product_searched:
        return True
    return False

async def service_validate_product_code(product_code):
    product_searched = await get_product_by_code(product_code)
    if product_searched:
        return True
    return False