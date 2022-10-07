
from src.server.database import connect_db, db, disconnect_db
from bson.objectid import ObjectId

async def get_all_products(skip=0, limit=2):
    await connect_db()
    
    product_collection = db.product_collection 
    
    try:
        products_cursor = product_collection.find().skip(int(skip)).limit(int(limit))
        products = await products_cursor.to_list(length=int(limit))
        if len(products) == 0:
            return False
        for product in products:
            product.pop("_id")
        return products
        
    except Exception as e:
        print(f'get_all_product.error: {e}')
        
    
    await disconnect_db()