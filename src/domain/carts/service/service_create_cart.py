from http.client import HTTPException
from src.domain.carts.models.create_new_cart import create_new_cart
from src.domain.carts.service.service_get_opened_cart_by_user_email import service_get_open_carts_by_user_email
from src.domain.users.service.service_get_user_by_email import service_get_user_by_email

async def service_create_cart(cart, user_email):
    
    cart_dict = cart.dict()
    
    #primeiro validar se usuário existe através do seu email
    user_searched = await service_get_user_by_email (user_email)  
    if user_searched == False:
        return {'There is no user associated with this email address'}
    #Se usuário existe busque seus carrinhos abertos
    user_open_cart = await service_get_open_carts_by_user_email(user_searched['email'])
    if user_open_cart == False:
        # Não havendo carrinho aberto, crie um novo
        cart_dict['user_email'] = user_searched['email'] 
        new_cart = await create_new_cart(cart_dict)
        return new_cart
    return user_open_cart
