from src.domain.products.models.create_product import create_product
from src.domain.schemas.product import ProductSchema
from src.domain.products.service.service_validate_product import service_validate_product_code, service_validate_product_name


async def service_create_new_product(product: ProductSchema):
    try:
        product_dict = product.dict()
        
        validate_name = await service_validate_product_name(product_dict["name"])
        validate_code = await service_validate_product_code(product_dict["code"])

        if validate_code == False and validate_name == False:
            result = await create_product(product_dict)
            return result
    
    except Exception as e:
        return {f'create_product_error {e}'} 

