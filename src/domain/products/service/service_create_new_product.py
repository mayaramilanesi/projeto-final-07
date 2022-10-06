from src.domain.products.models.create_product import create_product
from domain.schemas.product import ProductSchema



async def service_create_new_product(product: ProductSchema):
    product_dict = product.dict()
    #Validacoes de Produto....
    result = await create_product(product_dict)
    return result

