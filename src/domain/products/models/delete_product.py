
from src.server.database import db, connect_db, disconnect_db

async def delete_product(product_code):
    try:
        await connect_db()
        
        products_collection = db.products_collection
        
        product = await products_collection.delete_one({"code": product_code})
        if product.deleted_count:
            return True
        return False
    
    except Exception as e:
        return (f'delete_user.error: {e}')
    
    finally:
        await disconnect_db()