from itertools import product
from bson.decimal128 import Decimal128
from bson.objectid import ObjectId
from src.server.database import db, connect_db, disconnect_db

async def create_new_cart(cart):
    try:
        await connect_db()
        carts_collection = db.carts_collection
        
        cart["total_price"] = Decimal128(cart["total_price"])
        result = await carts_collection.insert_one(cart)
            
        if result.inserted_id:
            return result
        return False
        
    except Exception as e:
        print(f'create_cart.error: {e}')
        return False

    finally:
        await disconnect_db()
# async def get_order(carts_collection, order_id):
#     try:
#         order = await carts_collection.find_one({'_id': order_id})
#         if order:
#             return order
#     except Exception as e:
#         print(f'get_order.error: {e}')
#         return None