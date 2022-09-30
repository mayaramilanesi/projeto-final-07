from bson.objectid import ObjectId

async def delete_address(address_collection, address_list_id):
	try:
		address = await address_collection.delete_one(
			{'_id': address_list_id}
		)
		if address.deleted_count:
			return {'status': 'Address deleted'}
	except Exception as e:
		print(f'delete_address.error: {e}')