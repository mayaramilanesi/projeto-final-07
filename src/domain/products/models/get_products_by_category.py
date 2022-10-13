from src.server.database import connect_db, db, disconnect_db
from src.util.service import format_json

async def get_products_by_category(product_category, skip=0, limit=2):
    try:
        await connect_db()
        
        products_collection = db.products_collection 

        products_cursor = products_collection.find({"category": product_category}).skip(int(skip)).limit(int(limit))
        products = await products_cursor.to_list(length=int(limit))
        
        if len(products) == 0:
            return False
        products_json = format_json(products)
        return products_json
                     
    except Exception as e:
        return (f'get_products_by_category.error: {e}')       
    
    finally:
        await disconnect_db()