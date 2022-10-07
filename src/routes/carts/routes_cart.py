""" from typing import List

import src.domain.schemas.order as order
from fastapi import APIRouter, status
from src.domain.schemas.order import (OrderSchema)

routes_cart = APIRouter(
    prefix="/api/order"
)


@routes_order.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=OrderSchema,
)
async def create_new_order(order: OrderSchema):
    # Cria nova música
    new_order = await order.models.create_orders.create_open_order(order)
    return new_order


@routes_order.delete(
    "/{order_id}",
    # Código HTTP infomando que foi removido
    status_code=status.HTTP_202_ACCEPTED
)
async def remove_order(order_id):
    # Remove uma música pelo código
    await order.models.create_orders.delete_order(order_id) """