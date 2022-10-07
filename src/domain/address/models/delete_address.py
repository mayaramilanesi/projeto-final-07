from src.server.database import connect_db, db, disconnect_db

async def delete_address(address_id):
	try:
		await connect_db()
		address_collection = db.address_collection
  
		address_deleted = await address_collection.delete_one(
			{'_id': address_id}
		)
		if address_deleted.deleted_count:
			return True
		else:
			return False

	except Exception as e:
		print(f'delete_address.error: {e}')
  
	await disconnect_db()