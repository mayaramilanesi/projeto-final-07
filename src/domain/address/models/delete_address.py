from src.server.database_conexão_mongo import connect_db, db, disconnect_db

async def delete_address(address_collection, address_id):
	try:
		await connect_db()
		address_collection = db.address_collection
  
		address = await address_collection.delete_one(
			{'_id': address_id}
		)
		if address.deleted_count:
			return {'status': 'Address deleted'}

		await disconnect_db()
  
	except Exception as e:
		print(f'delete_address.error: {e}')