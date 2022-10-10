from src.domain.products.models.get_product_by_code import get_product_by_code
from src.domain.products.service.service_validate_product import service_validate_product_code


async def service_get_product_by_code(product_code):   
    try:
        product = await get_product_by_code(product_code)
        if product == False:
            return False
        return product
    except Exception as e:(f'get_all_products_error {e}')
