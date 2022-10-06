from src.domain.schemas.product import ProductSchema, ProductUpdatedSchema
from src.domain.products.models.update_product import update_product



#Ainda não está ajustado de acordo com a arquitetura e regras que definimos 
async def service_update_product(product: ProductUpdatedSchema):
        ...
