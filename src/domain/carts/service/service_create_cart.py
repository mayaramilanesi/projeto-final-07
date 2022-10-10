from src.domain.carts.models.create_new_cart import create_new_cart
from src.domain.carts.models.get_opened_cart_by_email import get_opened_cart_by_user_email
from src.domain.schemas.cart import CartSchema


async def service_create_cart(cart: CartSchema):
    data_user = await get_opened_cart_by_user_email(cart.user.email)
    if data_user == False:
        result = await create_new_cart(cart.dict())
        return result
    return data_user