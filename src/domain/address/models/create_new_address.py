from bson.objectid import ObjectId
from src.domain.schemas.address import AddressSchema
from pprint import pprint

from src.server.database_conexão_mongo import connect_db, db, disconnect_db

async def create_new_address(address_collection, address: AddressSchema):
    try:
        await connect_db()
        address_collection = db.address_collection
        
        address = await address_collection.insert_one(address)

        if address.inserted_id:
            return address
        
        await disconnect_db()     

    except Exception as e:
        print(f'create_new_address.error: {e}')
        
        
      