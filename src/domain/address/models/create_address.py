from src.server.database import connect_db, db, disconnect_db


async def create_address(address):
	try:
		await connect_db()
		address_collection = db.address_collection

		filter = {"user" : address["user"]} 
		new_value = { "$addToSet": {
				"address": {"$each": address["address"]}
				}
			}

		new_address = await address_collection.update_one(filter, new_value)
  
		if new_address.matched_count >= 1:
			return True
		else:
			return False

	except Exception:
		raise Exception("Internal error failure")  
	finally:
        	await disconnect_db()