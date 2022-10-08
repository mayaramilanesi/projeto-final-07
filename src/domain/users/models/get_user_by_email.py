from src.server.database import db, connect_db, disconnect_db
from pydantic import ValidationError

async def get_user_by_email(email):
    await connect_db()
    users_collection = db.users_collection 
    try:
        user = await users_collection.find_one({'email': email})
        return user
    except Exception as e:
        print(f'get_user.error: {e}')
    
    await disconnect_db()