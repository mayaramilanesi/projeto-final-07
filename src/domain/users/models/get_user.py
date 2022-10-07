from src.server.database import db, connect_db, disconnect_db
from pydantic import ValidationError

async def get_user(users_collection, user_id):
    await connect_db()
    try:
        data = await users_collection.find_one({'_id': user_id})
        if data:
            return data
    except Exception as e:
        print(f'get_user.error: {e}')
    
    await disconnect_db()