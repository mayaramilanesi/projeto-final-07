from src.server.database import db, connect_db, disconnect_db

async def closed_cart(opened):
    await connect_db()
    carts_collection = db.carts_collection
    filter = {
        opened: True
    }
    updated_record = {
        "$set": False
    }
    cart = await carts_collection.update_one(filter, updated_record)
    await disconnect_db()
    return cart