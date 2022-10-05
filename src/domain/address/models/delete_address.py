

async def delete_address(address_collection, address_id):
	try:
		address = await address_collection.delete_one(
			{'_id': address_id}
		)
		if address.deleted_count:
			return {'status': 'Address deleted'}
	except Exception as e:
		print(f'delete_address.error: {e}')