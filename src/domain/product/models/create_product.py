from src.domain.product.models.get_product_by_name import get_product_by_name
#from fastapi import HTTPException, status
from src.server.database import db
from src.domain.schemas.product_schema import ProductSchema
from pydantic import ValidationError

async def create_product(product_collection, product):
    try:
        # product = product.dict(product)
        # product_searched = await get_product_by_name(product_collection, product['name'])
        
        # if product_searched == None:
        new_product = await product_collection.insert_one(product)
        if new_product.inserted_id:
                return {'mensagem': 'product successfully created'}
    except ValidationError as e:
        return {f'create_product_error', {e}}   
    except ValueError:
        return {'error message': 'invalid input'}
    
    except AttributeError:
        if product['price'] < 0.01:
            return {'error message': 'price must be a number greater than R$0.01'}
        elif product['inventory'] == 0:
            return {'error message': 'inventory must be value greater than 0'}
