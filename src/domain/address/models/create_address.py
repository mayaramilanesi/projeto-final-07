from bson.objectid import ObjectId
from src.domain.address.models.get_address_by_email import get_address_by_email

from src.server.database import connect_db, db, disconnect_db


async def create_address(address, email):
	try:
		await connect_db()
		address_collection = db.address_collection
  
		address_user = await get_address_by_email(address_collection, email)

		filter = {"_id" : address_user[0]["_id"]} 
		new_value = { "$addToSet": {
				"address": address["address"][0]
				}
			}

		new_address = await address_collection.update_one(filter, new_value)
  
		if new_address .inserted_id:
			return True
		else:
			return False

	except Exception as e:
		print(f'create_new_address.error: {e}')
  
	await disconnect_db()