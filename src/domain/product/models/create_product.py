#from fastapi import HTTPException, status
from src.server.database import db
from pydantic import ValidationError

async def create_product(product_collection, product):
    try:     
        new_product = await product_collection.insert_one(product)
        if new_product.inserted_id:
            return True
        else:
            return False
    except ValidationError as e:
        return {f'create_product_error', {e}}   
    except ValueError:
        return {'error message': 'invalid input'}
    
    except AttributeError:
        if product['price'] < 0.01:
            return {'error message': 'price must be a number greater than R$0.01'}
        elif product['inventory'] == 0:
            return {'error message': 'inventory must be value greater than 0'}
