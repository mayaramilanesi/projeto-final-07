from bson.objectid import ObjectId
from src.domain.address.models.get_address_by_email import get_address_by_email

async def create_address(address_collection, address, email):
	try:
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

	except Exception as e:
		print(f'create_address.error: {e}')