
from src.server.database import db, connect_db, disconnect_db

async def delete_product(product_code):
    try:
        await connect_db()
        
        product_collection = db.product_collection
        
        product = await product_collection.delete_one({"code": product_code})
        if product.deleted_count:
            return True
        return False
    
    except Exception as e:
        return (f'delete_user.error: {e}')
    
    finally:
        await disconnect_db()