from src.server.database import connect_db, db, disconnect_db
from bson.objectid import ObjectId

async def add_order_number(email):
	try:
		await connect_db()
		carts_collection = db.carts_collection

		filter = {"user_email": email} 
		new_value = {"$set": {"order_number": ObjectId()}}

		new_order_number = await carts_collection.update_one(filter, new_value)
  
		if new_order_number.modified_count >= 1:
			return True
		else:
			return False

	except Exception:
		raise Exception("Internal error failure")  
	finally:
        	await disconnect_db()