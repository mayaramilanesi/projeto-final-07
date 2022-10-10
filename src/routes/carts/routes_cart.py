
from typing import List


from fastapi import APIRouter
from src.domain.schemas.cart import (CartSchema)
from src.domain.carts.service.service_create_cart import service_create_cart

routes_cart = APIRouter(
    prefix="/api/carts", tags=["Carts"]
)


@routes_cart.post("/")
async def create_new_cart(cart: CartSchema):
    # Cria novo carrinho
    # NÃO TESTADO = ERRO 404 NOT FOUND
    new_cart = await service_create_cart(cart)
    return new_cart


# @routes_order.delete(
#     "/{order_id}",
#     # Código HTTP infomando que foi removido
#     status_code=status.HTTP_202_ACCEPTED
# )