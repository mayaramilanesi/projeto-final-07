from pydantic import EmailStr
from src.server.database import db, connect_db, disconnect_db

async def get_opened_cart_by_user_email(email):
    await connect_db()
    carts_collection = db.carts_collection 
    try:
        cart = await carts_collection.find_one({'email': email, 'opened': True})
        await disconnect_db()
        return cart
        # if cart:
        #     return True
    except Exception as e:
        print(f'get_cart.error: {e}')
        return False