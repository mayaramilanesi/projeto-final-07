from src.domain.products.models.get_all_products import get_all_products



async def service_get_all_products():
    all_products = await get_all_products()
    if all_products == False:
        return False 
    return all_products

