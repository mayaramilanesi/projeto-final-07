
from fastapi import APIRouter

from src.domain.schemas.product import ProductSchema, ProductUpdatedSchema
from src.domain.products.service.service_get_product_by_code import service_get_product_by_code
from src.domain.products.service.service_create_new_product import service_create_new_product
from src.domain.products.service.service_get_product_by_category import get_products_by_category
from src.domain.products.service.service_update_product import service_update_product
from src.domain.products.service.service_get_all_products import service_get_all_products
from src.domain.products.service.service_delete_product import service_delete_product


rota_products = APIRouter(
    # Prefixo para o caminho da rota
    prefix="/api/products", tags=["Products"]
)


@rota_products.post("/new")
async def create_new_product(product: ProductSchema):
    result = await service_create_new_product(product)
    if result == True:
        return {'mensagem': 'product successfully created'}
    else:
        return {'mensagem': 'create new product failed'}

        
@rota_products.get("/{code}")
async def get_product_by_code(code: str):
    product_searched = await service_get_product_by_code(code)
    if product_searched == False:
        return {f'message': 'Product not found'}
    else:
        return product_searched

    
@rota_products.put("/{codigo}")
async def update_product(product: ProductUpdatedSchema):
   result = await service_update_product(product)
   return result   

    
# @rota_products.get("/all_products")
# async def get_all_products():
#     products_list = await service_get_all_products()
#     return products_list



# @rota_products.get("/{category}")
# async def get_products_by_category(product):
#     result = await service_get_product_by_category(category)
#     return result



# @rota_products.delete("/{codigo}")
# async def delete_product(product: ProductSchema):
#     result = await service_delete_product(product)
#     return result
#     ...