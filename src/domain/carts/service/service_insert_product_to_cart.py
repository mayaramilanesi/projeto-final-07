from src.domain.carts.service.service_get_opened_cart_by_user_email import service_get_open_carts_by_user_email
from src.domain.schemas.product import ProductCartSchema
from src.domain.carts.service.service_validate_product_quantity import service_validate_product_quantity
from src.domain.products.service.service_get_product_by_code import service_get_product_by_code
from src.domain.carts.service.service_calc_total_price import service_calc_total_price

from src.domain.carts.models.insert_product_to_cart import insert_product_to_cart

async def service_insert_product_to_cart(user_email, product_code, product_quantity):
    
    #Buscar produto
    product_searched = await service_get_product_by_code(product_code)
    
    #Se o produto existe, valida se a quantidade requerida está disponível em estoque
    if product_searched != False:
        validate_quantity = await service_validate_product_quantity(product_searched['code'], product_quantity)
        
        if validate_quantity == True:    
            cart_searched = await service_get_open_carts_by_user_email(user_email)

        
        new_product = ProductCartSchema(
            name=product_searched['name'],
            price=(product_searched['price']['$numberDecimal']),
            quantity=product_quantity,
            code=product_searched['code'])    
        
        if cart_searched != False:
          await insert_product_to_cart(cart_searched, new_product)
          cart_update = await service_calc_total_price(cart_searched)
        return cart_update

    