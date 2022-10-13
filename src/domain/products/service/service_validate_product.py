
from src.domain.products.models.get_product_by_name import get_product_by_name
from src.domain.products.models.get_product_by_code import get_product_by_code


async def service_validate_product_name(product_name):
    product_searched = await get_product_by_name(product_name)
    if product_searched == True:
        return True
    return False

async def service_validate_product_code(product_code):
    product_code = await get_product_by_code(product_code)
    if product_code == False:
        return True
    return False

async def service_validate_product_price(product_price):
    if product_price >= 0.01:
        return True
    return False