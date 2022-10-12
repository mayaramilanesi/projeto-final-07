from src.server.database import db, connect_db, disconnect_db

async def delete_all_carts(email):
    await connect_db()
    carts_collection = db.carts_collection
    
    try:
        order = await carts_collection.delete_many({'user_email': email})

        if order.deleted_count:
            return {'status': 'Cart deleted'}
        return False
    except Exception as e:
        print(f'delete_order.error: {e}')
    finally: 
        await disconnect_db()