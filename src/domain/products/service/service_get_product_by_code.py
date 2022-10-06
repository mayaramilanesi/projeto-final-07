from src.domain.products.models.get_product_by_code import get_product_by_code



async def service_get_product_by_code(product_code):
    product = await get_product_by_code(product_code)
    product.pop("_id")
    return product
