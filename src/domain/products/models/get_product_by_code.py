from src.server.database import db, connect_db, disconnect_db
from src.util.service import format_json


async def get_product_by_code(product_code):
    try:
        await connect_db()
        products_collection = db.products_collection
        data = await products_collection.find_one({"code": product_code})
        
        if data:
            data_json = format_json(data)    
            return data_json    
        return False
           
    except Exception as e:
        print(f'get_product.error: {e}')
    
    await disconnect_db()