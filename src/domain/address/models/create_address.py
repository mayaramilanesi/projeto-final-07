from bson.objectid import ObjectId
from src.domain.address.models.get_address_by_email import get_address_by_email

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

	except Exception as e:
		print(f'create_new_address.error: {e}')
  
	await disconnect_db()