from src.server.database import connect_db, db, disconnect_db


async def get_all_address(skip=0, limit=2):
      
      await connect_db()
      address_collection = db.address_collection
      
      try:
        address_cursor = address_collection.find().skip(int(skip)).limit(int(limit))
        address = await address_cursor.to_list(length=int(limit))
        if len(address) == 0:
            return False
        for a in address:
            a.pop("_id")
        return address
            
      except Exception as e:
            print(f'find_address.error: {e}')
            
      await disconnect_db()