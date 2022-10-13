from src.domain.carts.service.service_get_opened_cart_by_user_email import service_get_open_carts_by_user_email
from src.domain.carts.models.delete_product_from_cart import delete_product_from_cart
from src.domain.carts.service.service_calc_total_price import service_calc_total_price

from src.domain.carts.models.insert_product_to_cart import insert_product_to_cart

async def service_delete_product_from_cart(user_email, product_code, product_quantity):
  
    cart_searched = await service_get_open_carts_by_user_email(user_email)

    products = []    
    for product in cart_searched['products']:
        if(product['code'] == product_code):
            product['quantity'] = product['quantity'] - product_quantity
            if(product['quantity'] > 0):
                products.append(product) 
        else:
            products.append(product) 
            
    cart_searched['products'] = products            
    
    if cart_searched == None:
        return {'status': False, 'message': 'No open carts found for this email address'}
    #RETORNOS ERRADOS PARA CORRIGIR#    
    await delete_product_from_cart(cart_searched, product_code)
    cart_update = await service_calc_total_price(cart_searched)
    return {'status': True, 'message': 'No open carts found for this email address'}

    