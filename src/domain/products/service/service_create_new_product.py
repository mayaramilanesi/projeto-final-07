
from src.domain.products.models.create_product import create_product
from src.domain.schemas.product import ProductSchema
from src.domain.products.service.service_validate_product import service_validate_product_code, service_validate_product_name


async def service_create_new_product(product: ProductSchema):
    product_dict = product.dict()
    result = await create_product(product_dict)
    # validate_name = await service_validate_product_name(product_dict["name"])
    # if validate_name == True: 
    #     return False 
    
    # validate_code = await service_validate_product_code(product["code"])
    # if validate_code == True:
        # result = await create_product(product_dict)
    return result

