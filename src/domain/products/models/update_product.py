from src.server.database import db, connect_db, disconnect_db

async def update_product(product_code, product_data):
    try:
        await connect_db()
        
        products_collection = db.products_collection
        data = {k: v for k, v in product_data.items() if v is not None}
        product =  await products_collection.update_one(
            {'code': product_code},
            {'$set': data}
            
        )
       
        if product.modified_count:
            return True
        return False
    except Exception as e:
        print(f'update_product.error: {e}')
        
        await disconnect_db()
        
