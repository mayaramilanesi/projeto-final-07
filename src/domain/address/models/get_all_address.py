from src.server.database_conexão_mongo import connect_db, db, disconnect_db

async def get_all_address(address_collection):
      try:
            
            await connect_db()
            address_collection = db.address_collection
            
            address = await address_collection.find({})

            if address:
                  return address
            
            await disconnect_db()

      except Exception as e:
            print(f'find_address.error: {e}')