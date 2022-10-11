# Criar uma rota para cada arquivo?
from fastapi import APIRouter
from src.domain.carts.service.service_closed_cart import service_closed_cart
from fastapi import HTTPException, status


routes_carts_mayara = APIRouter(
    prefix="/api/address",
    tags=["Address"]
)

@routes_carts_mayara.put("/{email}", 
    summary="Closing the cart", 
    description="Route to close a cart that is open",
    status_code=status.HTTP_200_OK)

async def closing_cart(email):
    result = await service_closed_cart(email)
    if result == True:
        return {'mensagem': 'cart closed successfully'}
    else:
        raise HTTPException(status_code=404, detail="Cart not found.")