from src.server.database import db, connect_db, disconnect_db

async def delete_user(email):
    try:
        await connect_db()
        
        users_collection = db.users_collection
        
        user = await users_collection.delete_one({"email": email})
        
        if user.deleted_count:
            return True
        return False
    
    except Exception as e:
        return (f'delete_user.error: {e}')
    
    finally:
        await disconnect_db()