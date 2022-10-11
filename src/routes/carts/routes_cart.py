
from http.client import HTTPException
from typing import List


from fastapi import APIRouter
from pydantic import EmailStr
from src.domain.carts.service.service_get_opened_cart_by_user_email import service_get_open_carts_by_user_email
from src.domain.carts.service.service_delete_open_carts_by_user_email import service_delete_open_carts_by_user_email
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

@routes_cart.delete("/delete/{email}")
async def service_delete_(user_email: EmailStr):
    cart = await service_delete_open_carts_by_user_email(user_email)
    if cart == False:
        raise HTTPException(status_code=404, detail="Error")
    return cart
    
        
@routes_cart.get("/{email}")
async def get_cart_by_user_email(user_email: EmailStr):
    cart = await service_get_open_carts_by_user_email(user_email)
    if cart == False:
        raise HTTPException(status_code=404, detail="No carts found for this user")
    return cart
    