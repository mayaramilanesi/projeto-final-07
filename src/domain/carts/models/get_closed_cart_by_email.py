from src.server.database import db, connect_db, disconnect_db
from src.util.service import format_json

async def get_closed_cart_by_user_email(user_email, skip=0, limit=10):
    try:
        await connect_db()
        
        carts_collection = db.carts_collection 

        search_cursor = carts_collection.find({'user_email': user_email, 'opened': False}).skip(int(skip)).limit(int(limit))
        closed_carts = await search_cursor.to_list(length=int(limit))
        
        if len(closed_carts) == 0:
            return False

        return format_json(closed_carts)
                     
    except Exception as e:
        return (f'get_closed_carts_by_user_email: {e}')       
    finally:
        await disconnect_db()