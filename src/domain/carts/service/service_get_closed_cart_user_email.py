from src.domain.carts.models.get_closed_cart_by_email import get_closed_cart_by_user_email

async def service_get_closed_carts_by_user_email(user_email):
    try: 
        closed_carts = await get_closed_cart_by_user_email(user_email)
        
        if closed_carts == None:
            return False
        return closed_carts
        
    except Exception as e:
            return (f'service_get_closed_carts_by_user_email: {e}')


async def service_get_closed_carts_quantity_by_user_email(user_email):
    try: 
        closed_carts = await get_closed_cart_by_user_email(user_email)
        closed_carts_quantity = len(closed_carts)
        
        if closed_carts == None:
            return False
        return {
            "closed_carts_quantity": closed_carts_quantity
        }
        
    except Exception as e:
            return (f'service_get_closed_carts_quantity_by_user_email: {e}')