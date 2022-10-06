from bson.objectid import ObjectId
from src.domain.address.models.get_address_by_email import get_address_by_email

from src.server.database import connect_db, db, disconnect_db


async def create_address(address_collection, address, email):
	try:
		await connect_db()
		address_collection = db.address_collection
		address_user = await get_address_by_email(address_collection, email)
		
		if not address_user:
			result = await address_collection.insert_one(address)
			return await result
		else:
			filter = {"_id" : address_user[0]["_id"]} # Verificar comportamento da função
			new_value = { "$addToSet": {
				"address": address["address"][0]
				}
			}

			await address_collection.update_one(filter, new_value)
			return await get_address_by_email(address_collection, email)
		await disconnect_db()

	except Exception as e:
		print(f'create_address.error: {e}')