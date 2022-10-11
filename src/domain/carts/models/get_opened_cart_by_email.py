
from src.server.database import db, connect_db, disconnect_db

async def get_opened_cart_by_user_email(user_email):
    try:
    
        await connect_db()
        carts_collection = db.carts_collection 
        cart_searched = await carts_collection.find_one({'user_email': user_email, 'opened': True})
    
        if cart_searched:
            return cart_searched
        return None
    
    except Exception as e:
            return (f'get_cart.error: {e}')
        
    finally:
        await disconnect_db()
    
