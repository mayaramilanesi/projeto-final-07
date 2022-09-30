from src.domain.schemas.address import Addressschema

async def get_address_by_email(address_collection, email):
	try:
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

	except Exception as e:
		print(f'get_address.error: {e}') 
  
  
 
 
 
 
