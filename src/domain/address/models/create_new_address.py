from src.server.database import connect_db, db, disconnect_db

async def create_new_address(address):
    try:
        await connect_db()
        address_collection = db.address_collection
        
        new_address = await address_collection.insert_one(address)

        if new_address.inserted_id:
            return True
        else:
            return False
        
    except Exception:
        raise Exception("Internal error failure")  
    finally:
        	await disconnect_db()
        
        
      