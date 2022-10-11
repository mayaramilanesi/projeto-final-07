from src.domain.carts.models.create_new_cart import create_new_cart
from src.domain.carts.models.get_opened_cart_by_email import get_opened_cart_by_user_email


async def service_create_cart(cart, user_email):
    
    cart_dict = cart.dict()
    #primeiro validar se usuário existe
    user_open_cart = await get_opened_cart_by_user_email(user_email)
    
    if user_open_cart == None:
        cart_dict['user_email'] = user_email
        result = await create_new_cart(cart_dict)
        return result
    return user_open_cart