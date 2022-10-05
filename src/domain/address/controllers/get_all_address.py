from bson.objectid import ObjectId
from pprint import pprint

from src.server.database_conexão_mongo import connect_db, db, disconnect_db

from src.domain.address.models.get_all_address import get_all_address


async def get_all_address(address_collection):
      await connect_db()
      
      address_collection = db.address_collection

      all_address = await get_all_address(address_collection)
      pprint(all_address)
            
      await disconnect_db()
            
