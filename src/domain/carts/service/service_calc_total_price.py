from itertools import product
from src.domain.carts.models.get_opened_cart_by_email import get_opened_cart_by_user_email
from src.domain.carts.models.update_quantity_cart import update_quantity_cart

async def service_calc_total_price(cart):
    try: 
        open_carts = await get_opened_cart_by_user_email(cart['user_email'])
        
        if open_carts == None:
            return False
        
        total_price = 0
        quantity = 0
        
        for product  in open_carts['products']:
            total_price += product['price'] * product['quantity']
            quantity += product['quantity']
        
        open_carts['total_quantity'] = quantity
        open_carts['total_price'] = total_price
        
        cart_updated = await update_quantity_cart(open_carts)
        
        if cart_updated == None:
            return False
        return cart_updated
    except Exception as e:
            return (f'get_open_carts_by_user_email: {e}')