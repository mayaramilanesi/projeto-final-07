#from fastapi import HTTPException, status
from src.server.database import db, connect_db, disconnect_db
from pydantic import ValidationError
from bson.decimal128 import Decimal128

async def create_product(product):
    await connect_db()
    
    product_collection = db.product_collection 
    
    try:
        product["price"] = Decimal128(product["price"])     
        new_product = await product_collection.insert_one(product)
        if new_product.inserted_id:
            return True
        else:
            return False
    
    except Exception as e:
        print({f'create_product_error', {e}})  

    await disconnect_db()