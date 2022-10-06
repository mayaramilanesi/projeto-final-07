from src.domain.products.models.get_product_by_name import get_product_by_name
from src.domain.schemas.product import ProductSchema



async def service_validate_product(product: ProductSchema):
    
    product = product.dict()
    product_searched = await get_product_by_name(db.product_collection, product["name"])
    
    if product_searched:
        return False
 
    new_product = await create_product(product)
    if new_product == None:
        return {'message': 'Create product error' }
    return new_product
    
