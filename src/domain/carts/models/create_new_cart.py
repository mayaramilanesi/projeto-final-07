from itertools import product
from re import U
from bson.objectid import ObjectId
from src.domain.schemas.cart import CartSchema
from src.server.database import db, connect_db, disconnect_db

async def create_new_cart(cart):
    await connect_db()
    carts_collection = db.carts_collection
    try:
        cart = await carts_collection.insert_one(cart)
        await disconnect_db()
        
        if cart:
            return cart
    except Exception as e:
        print(f'create_cart.error: {e}')
        return False

# async def get_order(carts_collection, order_id):
#     try:
#         order = await carts_collection.find_one({'_id': order_id})
#         if order:
#             return order
#     except Exception as e:
#         print(f'get_order.error: {e}')
#         return None