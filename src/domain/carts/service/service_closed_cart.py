from src.domain.carts.models.closed_cart import closed_cart
from src.domain.carts.models.add_order_number import add_order_number
from src.domain.address.models.get_address_delivery_true import get_address_delivery_true
from src.util.service import format_json

async def service_closed_cart(email):

      cart = await closed_cart(email)
      if cart:
            await add_order_number(email)
            result = format_json(await get_address_delivery_true(email))
            return result

      return cart
      
