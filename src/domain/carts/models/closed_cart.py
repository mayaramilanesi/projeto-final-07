from src.server.database import db, connect_db, disconnect_db

async def closed_cart(email):
    try:
        await connect_db()
        carts_collection = db.carts_collection
        
        filter = {"user": email}
        updated_record = {"$set": {"opened": False}}
        
        cart = await carts_collection.update_one(filter, updated_record)
    
        if cart:
            return True
        else:
            return False
        
    except Exception:
        raise Exception("Internal error failure")  
    finally:
        	await disconnect_db()