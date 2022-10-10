
from src.server.database import connect_db, db, disconnect_db

async def get_address_by_email(email):
	try:
		await connect_db()
		
		address_collection = db.address_collection
		user_address =  address_collection.aggregate([
			{
				"$match":{ 
           				"user": email	
				}
			}
		])

		if user_address:
			return await user_address.to_list(1)
		else:
			return False

	except Exception:
		raise Exception("Internal error failure")  
	finally:
        	await disconnect_db()
  
  
 
 
 
 
