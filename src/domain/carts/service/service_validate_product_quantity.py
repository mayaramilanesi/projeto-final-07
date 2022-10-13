from src.domain.products.service.service_get_product_by_code import service_get_product_by_code


async def service_validate_product_quantity(product_code, quantity): 
    
    product_searched = await service_get_product_by_code(product_code)
    if quantity <= product_searched['inventory']:
        return True
    return False
