
from src.domain.schemas.product import ProductSchema
from src.domain.schemas.cart import CartSchema
from src.domain.carts.service.service_validate_product_quantity import service_validate_product_quantity
from src.domain.products.service.service_get_product_by_code import service_get_product_by_code
from src.domain.carts.models.get_opened_cart_by_email import get_opened_cart_by_user_email

async def insert_product_to_cart(user_email, product_code, product_quantity):
    
    #Buscar produto
    product_searched = await service_get_product_by_code(product_code)
    #Se o produto existe, valida se a quantidade requerida 
    if product_searched:
        await service_validate_product_quantity(product_searched['code'], product_quantity)
      
    cart_searched = await get_opened_cart_by_user_email(user_email)
    if cart_searched:
        cart_searched['products']
    