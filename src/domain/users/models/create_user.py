from src.server.database import db, connect_db, disconnect_db


async def create_user(user):
    
    await connect_db()
    users_collection = db.users_collection 
    
    try:
        user = await users_collection.insert_one(user)

        if user.inserted_id:
            return True
        else:
            return False
    
    except Exception:
        raise Exception("Internal error failure")  
    finally:
        	await disconnect_db()