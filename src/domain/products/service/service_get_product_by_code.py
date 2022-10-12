from src.domain.products.models.get_product_by_code import get_product_by_code
from src.util.service import format_json

async def service_get_product_by_code(product_code):   
    try:
        product = await get_product_by_code(product_code)
        if product == False:
            return False
        return format_json(product)
    except Exception as e:(f'get_all_products_error {e}')
