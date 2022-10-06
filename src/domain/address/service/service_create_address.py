from bson.objectid import ObjectId
from pprint import pprint

from src.server.database import connect_db, db, disconnect_db

from src.domain.address.models.get_address_by_email import get_address_by_email
from src.domain.address.models.create_new_address import create_new_address
from src.domain.address.models.create_address import create_address



async def create_address(address_collection, address, email):

      address_user = await get_address_by_email(address_collection, email)

      if not address_user:
            result = await create_new_address(address_collection, address)
            return result
      else:
            result = await create_address(address_collection, address)
            return result
