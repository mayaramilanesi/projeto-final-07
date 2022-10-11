from src.util.service import format_json
from bson.decimal128 import Decimal128
from src.server.database import db, connect_db, disconnect_db

async def create_new_cart(cart):
    try:
        await connect_db()
        carts_collection = db.carts_collection
        
        cart["total_price"] = Decimal128(cart["total_price"])
        result = await carts_collection.insert_one(cart)
            
        if result.inserted_id:
            return {'message': 'cart successfully created'}
        return False
        
    except Exception as e:
        return (f'create_cart.error: {e}')

    finally:
        await disconnect_db()
