
from http.client import HTTPException
from src.util.service import format_json
from fastapi import HTTPException, status

from fastapi import APIRouter
from pydantic import EmailStr
from src.domain.carts.service.service_get_opened_cart_by_user_email import service_get_open_carts_by_user_email
from src.domain.carts.service.service_delete_open_carts_by_user_email import service_delete_open_carts_by_user_email
from src.domain.schemas.cart import CartSchema
from src.domain.carts.service.service_create_cart import service_create_cart
from src.domain.carts.service.service_insert_product_to_cart import service_insert_product_to_cart
from src.domain.carts.service.service_delete_product_from_cart import service_delete_product_from_cart
from src.domain.carts.service.service_closed_cart import service_closed_cart
from src.domain.carts.service.service_get_closed_cart_user_email import service_get_closed_carts_by_user_email, service_get_closed_carts_quantity_by_user_email

routes_cart = APIRouter(
    prefix="/api/carts", tags=["Carts"]
)

@routes_cart.post("/",
    summary="Creating a new cart for an existing user account", 
    description="Route to create a cart for an user. By default the cart is created open and empty",
    status_code=status.HTTP_200_OK)
async def create_new_cart(cart: CartSchema, user_email: EmailStr):
    new_cart = format_json(await service_create_cart(cart, user_email))
    if new_cart == False:
        raise HTTPException(status_code=422, detail="Cart not created")
    return new_cart

@routes_cart.put("/insert/{code}",
    summary="Adding a product to an existing open cart", 
    description="Route do add a product to the user's open cart",
    status_code=status.HTTP_200_OK)
async def insert_product_in_cart(user_email: EmailStr, product_code: str, product_quantity: int):
        cart = await service_insert_product_to_cart(user_email, product_code, product_quantity)
        if cart['status'] == False:
            raise HTTPException(status_code=404, detail=cart['message'])
        return {"Product successfully inserted"}

# @routes_cart.put("/delete/{code}",
#     summary="Deleting a product from an existing open cart", 
#     description="Route do delete a product from an existing open cart",
#     status_code=status.HTTP_200_OK)
# async def delete_product_from_cart(user_email: EmailStr, product_code: str, product_quantity: int):
#     cart = await service_delete_product_from_cart(user_email, product_code, product_quantity)
#     if cart == False:
#         raise Exception
#     return {f'product successfully inserted'}


@routes_cart.delete("/delete/{email}",
    summary="Deleting user's open cart", 
    description="Route to delete a user's open cart",
    status_code=status.HTTP_200_OK)
async def service_delete_(user_email: EmailStr):
    cart = await service_delete_open_carts_by_user_email(user_email)
    if cart == False:
        raise HTTPException(status_code=404, detail="Error")
    return cart
    
        
@routes_cart.get("/{email}", 
    summary="Getting the user's open carts", 
    description="Route to get a user's open cart",
    status_code=status.HTTP_200_OK)
async def get_open_carts_by_user_email(user_email: EmailStr):
    cart = await service_get_open_carts_by_user_email(user_email)
    if cart == False:
        raise HTTPException(status_code=404, detail="No carts found for this user")
    return cart

@routes_cart.put("/{email}", 
    summary="Closing an open cart", 
    description="Route to close a cart that is open",
    status_code=status.HTTP_200_OK)

async def closing_cart(email):
    result = await service_closed_cart(email)
    if result == True:
        return {'mensagem': 'cart closed successfully'}
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