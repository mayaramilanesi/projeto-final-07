from src.server.database import db, connect_db, disconnect_db
from pydantic import ValidationError
from src.domain.users.models import get_user


async def create_user(users_collection, user):
    await connect_db()
    users_collection = db.users_collection 
    try:
        user = await users_collection.insert_one(user)

        if user.inserted_id:
            user = await get_user(users_collection, user.inserted_id)
            return user
    
    except Exception as e:
        return {f'create_user_error', {e}}  
     
    await disconnect_db()