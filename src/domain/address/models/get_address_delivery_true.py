from src.util.service import format_json
from src.server.database import db, connect_db, disconnect_db

async def get_address_delivery_true(email):
      try: 
            await connect_db()
            address_collection = db.address_collection 
            search_cursor = await address_collection.find_one({'user': email, 'address.is_delivery': True})

            if not search_cursor:
                  return False
            
            for s in search_cursor['address']:
                  if s['is_delivery']:
                        return s
                     
      except Exception as e:
        return (f'get_address_delivery_true: {e}')       
      finally:
        await disconnect_db()