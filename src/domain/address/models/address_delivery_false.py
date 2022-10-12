from src.server.database import db, connect_db, disconnect_db

async def address_delivery_false(email):
    try:
        await connect_db()
        address_collection = db.address_collection
        
        filter = {"user": email,"address.is_delivery": True}
        update = {"$set": {"address.$.is_delivery": False}}
        
        address = await address_collection.update_one(filter, update)
        
        if address.modified_count:
            return True
        else:
            return False
        
    except Exception as e:
        raise Exception("Internal error failure", e)  
    finally:
        	await disconnect_db()