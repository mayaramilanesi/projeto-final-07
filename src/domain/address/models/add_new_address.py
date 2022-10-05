from bson.objectid import ObjectId
from src.domain.address.models.get_address_by_email import get_address_by_email
from src.domain.schemas.address import AddressSchema


async def add_new_address(address_collection, address: AddressSchema, email):
	try:
		address_user = await get_address_by_email(address_collection, email)
  
		filter = {"_id" : address_user[0]["_id"]} 
		new_value = { "$addToSet": {
				"address": address["address"][0]
			}
		}

		await address_collection.update_one(filter, new_value)
		return await get_address_by_email(address_collection, email)

	except Exception as e:
		print(f'create_address.error: {e}')