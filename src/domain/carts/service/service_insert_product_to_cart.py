from src.domain.carts.service.service_get_opened_cart_by_user_email import service_get_open_carts_by_user_email
from src.domain.schemas.product import ProductCartSchema
from src.domain.carts.service.service_validate_product_quantity import service_validate_product_quantity
from src.domain.products.service.service_get_product_by_code import service_get_product_by_code
from src.domain.carts.service.service_calc_total_price import service_calc_total_price
from src.domain.users.service.service_get_user_by_email import service_get_user_by_email
from src.domain.carts.models.insert_product_to_cart import insert_product_to_cart


async def service_insert_product_to_cart(user_email, product_code, product_quantity):
    user_searched = await service_get_user_by_email(user_email)
    if user_searched == False:
        return {'status': False, 'message': 'User not found'}
    
    product_searched = await service_get_product_by_code(product_code)
    if product_searched == False:
        return {'status': False, 'message': 'Product not found'}
    
    validate_quantity = await service_validate_product_quantity(product_searched['code'], product_quantity)
    if validate_quantity == False:
        return {'status': False, 'message': 'Quantity required is greater than available'}
    
    cart_searched = await service_get_open_carts_by_user_email(user_email)
    if cart_searched == False:
        return {'status': False, 'message': 'Open cart not found. You should create a new cart first'}
        
    new_product = ProductCartSchema(
        name=product_searched['name'],
        price=(product_searched['price']['$numberDecimal']),
        quantity=product_quantity,
        code=product_searched['code'])    
        
    product_inserted = await insert_product_to_cart(cart_searched, new_product)
    if product_inserted == True: 
        await service_calc_total_price(cart_searched)
        return {'status': True, 'message': 'Product inserted successfully'}
    return {'status': False, 'message': 'Insert product failed'}

    