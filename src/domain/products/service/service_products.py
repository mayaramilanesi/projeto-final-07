from typing import List
from domain.schemas.product import ProductSchema, ProductUpdatedSchema
from src.domain.product.models.get_all_products import get_all_products
from src.domain.product.models.get_product_by_name import get_product_by_name
from src.domain.product.models.get_product_by_code import get_product_by_code
from src.domain.product.models.create_product import create_product
from src.domain.product.models.update_product import update_product
from src.domain.product.models.delete_product import delete_product
from src.domain.product.models.get_products_by_category import get_products_by_category
from bson.objectid import ObjectId


from src.server.database import db, connect_db, disconnect_db 

async def service_validate_product( product: ProductSchema):
    
    product = product.dict()
    product_searched = await get_product_by_name(db.product_collection, product["name"])
    
    if product_searched:
        return False
 
    new_product = await create_product(product)
    if new_product == None:
        return {'message': 'Create product error' }
    return new_product
    

    
    
async def service_create_new_product(product: ProductSchema):
    product_dict = product.dict()
    #Validacoes de Produto....
    result = await create_product(product_dict)
    return result


async def service_get_product_by_code(product_code):
    product = await get_product_by_code(product_code)
    product.pop("_id")
    return product

async def service_get_product_by_category(product_collection, product_category):
    products_list = []
    products = await get_products_by_category(product_collection, product_category)
    if products is not None:
        products_list.append(products)
        return products_list
    else:
        return {'message': 'No products found for category'}

async def service_get_all_products() -> List[dict]:
    all_products = await get_all_products()
    if all_products is None:
        return {'message': 'No products were found'}
    else: 
        return all_products


    


async def service_update_product(product: ProductUpdatedSchema):
        ...


async def service_delete_product(product_collection, product: ProductSchema):
        ...

