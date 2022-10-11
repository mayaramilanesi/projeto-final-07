
from http.client import HTTPException
from typing import List


from fastapi import APIRouter
from pydantic import EmailStr
from src.util.service import format_json
from src.domain.schemas.cart import CartSchema
from src.domain.carts.service.service_create_cart import service_create_cart
from src.domain.carts.service.service_validate_product_quantity import service_validate_product_quantity

routes_cart = APIRouter(
    prefix="/api/carts", tags=["Carts"]
)

@routes_cart.post("/")
async def create_new_cart(cart: CartSchema, user_email: EmailStr):
    new_cart = await service_create_cart(cart, user_email)
    if new_cart == False:
        raise HTTPException(status_code=404, detail="Cart not created")
    return new_cart

# @routes_cart.put("/{code}")
# async def insert_product_in_cart(user_email, product_code, quantity: int):
# user = await service_create_cart(user_email, product_code


# @routes_cart.delete("/")
# async def remove_product_in_cart(product_code, cart):
#     ...
    
# @routes_cart.get("/")
# async def get_all_carts():
#     ...