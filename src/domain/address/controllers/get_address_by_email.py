from bson.objectid import ObjectId
from pprint import pprint

from src.server.database_conexão_mongo import connect_db, db, disconnect_db

from src.domain.address.models.get_address_by_email import get_address_by_email



async def get_address_by_email(address_collection, email):
      await connect_db()
      
      address_collection = db.address_collection

      address_user = await get_address_by_email(address_collection, email)
      pprint(address_user)

      await disconnect_db()