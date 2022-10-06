
from src.server.database import connect_db, db, disconnect_db

async def get_address_by_email(address_collection, email):
	try:
		await connect_db()
		address_collection = db.address_collection()
  
		user_address =  address_collection.aggregate([
			{
				"$lookup":
					{      
						"from": "users_collection",
						"localField": "user_id",
						"foreignField": "_id",
						"as": "user_data"
					}
			},
			{
				"$match":{ 
           				"user_data.email": email	
				}
			}
		])

		return await user_address.to_list(1)

		await disconnect_db()

	except Exception as e:
		print(f'get_address.error: {e}') 
  
  
 
 
 
 
