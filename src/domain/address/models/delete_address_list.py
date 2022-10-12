from src.server.database import db, connect_db, disconnect_db

async def delete_address_list(email):
    try:
        await connect_db()
        
        address_collection = db.address_collection
        
        address_deleted = await address_collection.delete_one({"user": email})
        
        if address_deleted.deleted_count:
            return True
        return False
    
    except Exception as e:
        return (f'delete_user.error: {e}')
    
    finally:
        await disconnect_db()