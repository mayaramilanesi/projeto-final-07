
from fastapi import APIRouter

from src.domain.schemas.product import ProductSchema, ProductUpdatedSchema
from src.domain.products.service import service_create_new_product, service_update_product, service_delete_product, service_get_all_products, service_get_product_by_category, service_get_product_by_code, service_validate_product

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