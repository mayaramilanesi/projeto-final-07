
from http.client import HTTPException
from typing import List
from src.util.service import format_json
from fastapi import HTTPException, status


from fastapi import APIRouter
from pydantic import EmailStr
from src.domain.schemas.product import ProductCartSchema
from src.domain.carts.service.service_get_opened_cart_by_user_email import service_get_open_carts_by_user_email
from src.domain.carts.service.service_delete_open_carts_by_user_email import service_delete_open_carts_by_user_email
from src.domain.schemas.cart import CartSchema
from src.domain.carts.service.service_create_cart import service_create_cart
from src.domain.carts.service.service_insert_product_to_cart import service_insert_product_to_cart
from src.domain.carts.service.service_validate_product_quantity import service_validate_product_quantity
from src.domain.carts.service.service_closed_cart import service_closed_cart
from src.domain.carts.service.service_get_closed_cart_user_email import service_get_closed_carts_by_user_email, service_get_closed_carts_quantity_by_user_email

routes_cart = APIRouter(
    prefix="/api/carts", tags=["Carts"]
)

@routes_cart.post("/")
async def create_new_cart(cart: CartSchema, user_email: EmailStr):
    new_cart = format_json(await service_create_cart(cart, user_email))
    if new_cart == False:
        raise HTTPException(status_code=404, detail="Cart not created")
    return new_cart

@routes_cart.put("/insert/{code}")
async def insert_product_in_cart(user_email: EmailStr, product_code: str, product_quantity: int):
    cart = await service_insert_product_to_cart(user_email, product_code, product_quantity)
    if cart == False:
        raise Exception
    return {f'product successfully inserted'}


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


@routes_cart.put("/{email}", 
    summary="Closing the cart", 
    description="Route to close a cart that is open",
    status_code=status.HTTP_200_OK)

async def closing_cart(email):
    result = await service_closed_cart(email)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Cart not found.")
    
@routes_cart.get("/closed/{email}")
async def closed_cart_by_user_email(user_email: EmailStr):
    carts = await service_get_closed_carts_by_user_email(user_email)
    if carts == False:
        raise HTTPException(status_code=404, detail="No closed carts found for this user")
    return carts

@routes_cart.get("/closed/quantity/{email}")
async def closed_cart_quantity_by_user_email(user_email: EmailStr):
    carts = await service_get_closed_carts_quantity_by_user_email(user_email)
    if carts == False:
        raise HTTPException(status_code=404, detail="No closed carts found for this user")
    return carts