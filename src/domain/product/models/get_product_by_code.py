from src.server.database import db, connect_db, disconnect_db



from types import NoneType


async def get_product_by_code(product_code):
    try:
        await connect_db()
        product_collection = db.product_collection
        data = await product_collection.find_one({"code": product_code})
        if data:
            await disconnect_db()
            return data    
        else:
            await disconnect_db()
            return False
        
        
    except Exception as e:
        print(f'get_product.error: {e}')