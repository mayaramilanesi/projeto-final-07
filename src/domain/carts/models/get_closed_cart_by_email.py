from src.util.service import format_json
from src.server.database import db, connect_db, disconnect_db

async def get_closed_cart_by_user_email(user_email, skip=0, limit=10):
    try:
        await connect_db()
        
        carts_collection = db.carts_collection 

        search_cursor = carts_collection.find({'user_email': user_email, 'opened': False}).skip(int(skip)).limit(int(limit))
        closed_carts = await search_cursor.to_list(length=int(limit))
        
        if len(closed_carts) == 0:
            return False
        for closed_cart in closed_carts:
            closed_cart.pop("_id")
            closed_cart["total_price"] = str(closed_cart["total_price"])
        return closed_carts
                     
    except Exception as e:
        return (f'get_closed_carts_by_user_email: {e}')       
    finally:
        await disconnect_db()