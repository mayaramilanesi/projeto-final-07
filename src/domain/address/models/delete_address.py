from bson import ObjectId
from src.server.database import connect_db, db, disconnect_db

async def delete_address(address_id: ObjectId):
	try:
		await connect_db()
		address_collection = db.address_collection
  
		address_deleted = await address_collection.update_one({'address._id': ObjectId(address_id)}, {"$pull": {"address": {"_id": ObjectId(address_id)} }})
  
		if address_deleted.matched_count >= 1:
			return True
		else:
			return False

	except Exception as e:
		print(f'delete_address.error: {e}')
  
	await disconnect_db()