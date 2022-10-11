from src.server.database import db, connect_db, disconnect_db

async def delete_cart(user_email):
    await connect_db()
    carts_collection = db.carts_collection
    try:
        order = await carts_collection.delete_one(
            {'user_email': user_email,
             'opened': True}
        )

        if order.deleted_count:
            return {'status': 'Order deleted'}
        return False
    except Exception as e:
        print(f'delete_order.error: {e}')
    finally: 
        await disconnect_db()