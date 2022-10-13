from src.domain.products.models.create_product import create_product
from src.domain.schemas.product import ProductSchema
from src.domain.products.service.service_validate_product import service_validate_product_code, service_validate_product_name, service_validate_product_price


async def service_create_new_product(product: ProductSchema):
    try:
        
        product_dict = product.dict()
        
        validate_name = await service_validate_product_name(product_dict["name"])
        if validate_name == False:
            return {'status': False, 'message': 'A product with this name already exists'}
       
        validate_code = await service_validate_product_code(product_dict["code"])
        if validate_code == False:
            return {'status': False, 'message': 'A product with this code already exists'}
        
        validate_price = await service_validate_product_price(product_dict["price"])
        if validate_price == False:
            return {'status': False, 'message': 'Product price must be greater than R$0.01'}
        
        result = await create_product(product_dict)
        if result == False:
            return {'status': False, 'message': 'Impossible to create_product'}    
        return {'status': True, 'message': 'Product successfully created'}
    
    except Exception as e:
        return {f'create_product_error {e}'} 

