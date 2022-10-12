from src.domain.carts.models.closed_cart import closed_cart

async def service_closed_cart(email):

      cart = await closed_cart(email)

      return cart
      