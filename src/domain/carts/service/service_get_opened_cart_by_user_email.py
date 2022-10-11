from logging import exception
from src.domain.carts.models.get_opened_cart_by_email import get_opened_cart_by_user_email

async def service_get_open_carts_by_user_email(user_email):
    try: 
        open_carts = await get_opened_cart_by_user_email(user_email)
        if open_carts == None:
            return False
        return {'There is already a shopping cart associated with this user'}
    except Exception as e:
            return (f'get_open_carts_by_user_email: {e}')