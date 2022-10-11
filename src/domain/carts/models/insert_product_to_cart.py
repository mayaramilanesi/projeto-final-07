
from src.domain.schemas.product import ProductSchema
from src.domain.schemas.cart import CartSchema
from src.server.database import db, connect_db, disconnect_db
 

async def insert_product_to_cart(cart, product, quantity):
    try: 
        await connect_db()
        carts_collection = db.carts_collection
        
        data = {k: v for k, v in product_data.items() if v is not None}
        
    except Exception as e:
        return Exception(''
    finally:
    await disconnect_db()