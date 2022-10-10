from src.server.database import db, connect_db, disconnect_db

async def delete_cart(carts_collection, order_id):
    await connect_db()
    carts_collection = db.carts_collection
    try:
        order = await carts_collection.delete_one(
            {'_id': order_id}
        )
        await disconnect_db()
        if order.deleted_count:
            return {'status': 'Order deleted'}
    except Exception as e:
        print(f'delete_order.error: {e}')