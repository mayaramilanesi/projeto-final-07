from src.server.database import db, connect_db, disconnect_db

async def create_product(product):
    await connect_db()
    
    products_collection = db.products_collection 

    try: 
        new_product = await products_collection.insert_one(product)
        
        if new_product.inserted_id:
            return True
        return False
    
    except Exception:
        raise Exception("Internal error failure")  
    finally:
        await disconnect_db()