
from fastapi import FastAPI, APIRouter

from src.domain.schemas.product_schema import ProductSchema, ProductUpdatedSchema
from src.domain.product.controller.product_service import service_create_new_product, service_get_product_by_code, service_get_all_products, delete_product, service_update_product, service_validate_product

rota_products = APIRouter(
    # Prefixo para o caminho da rota
    prefix="/api/products"
)


@rota_products.post("/product", tags=["Product"])
async def create_new_product(product: ProductSchema):
    await service_create_new_product(product)
    
        
@rota_products.get("/{codigo}",tags=["Product"])
async def get_product_by_code(product_code: str):
    product_searched = await service_get_product_by_code(product_code)
    if product_searched == False:
        return {f'message': 'Product not found'}
    else:
        return product_searched

    
@rota_products.put("/{codigo}", tags=["Product"])
async def update_product(product: ProductUpdatedSchema):
   result = await service_update_product(product)
   return result   

    
# @rota_products.get("/", tags=["Product"])
# async def get_all_products():
#     products_list = await service_get_all_products()
#     return products_list



# @rota_products.get("/{category}", tags=["Product"])
# async def get_products_by_category(product):
#     result = await service_get_product_by_category(category)
#     return result



# @rota_products.delete("/{codigo}")
# async def delete_product(product: ProductSchema):
#     result = await service_delete_product(product)
#     return result
#     ...