from src.server.database import db, connect_db, disconnect_db
 
async def get_product_by_name(product_name):
    try:
        await connect_db()
        product_collection = db.product_collection
        data = await product_collection.find_one({'name': product_name})
        if data:
            return data
        else:
            return False
    
    except Exception as e:
        print(f'get_product.error: {e}')
    
    await disconnect_db()