from src.domain.products.models.get_products_by_category import get_products_by_category

async def service_get_product_by_category(product_category):
    try:
        products = await get_products_by_category(product_category)
        if products == False:
            return False
        return products
    
    except Exception as e:
        return {f'get_products_by_category_error {e}'}

