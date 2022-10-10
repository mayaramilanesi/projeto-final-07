from src.server.database import db, connect_db, disconnect_db
from pydantic import ValidationError
from src.domain.users.models import get_user


async def create_user(user):
    await connect_db()
    users_collection = db.users_collection 
    try:
        user = await users_collection.insert_one(user)
        await disconnect_db()

        if user.inserted_id:
            return True
        else:
            return False
    
    except Exception as e:
        return {f'create_user_error', {e}}  