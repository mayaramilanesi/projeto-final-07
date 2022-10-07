from src.server.database import connect_db, db, disconnect_db

async def get_all_address():
      try:
            
            await connect_db()
            address_collection = db.address_collection
            
            all_address = await address_collection.find({})

            if all_address:
                  return all_address
            else:
                  return False
            
      except Exception as e:
            print(f'find_address.error: {e}')
            
      await disconnect_db()