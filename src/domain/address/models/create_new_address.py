from bson.objectid import ObjectId
from src.domain.schemas.address import AddressSchema
from pprint import pprint

async def create_new_address(address_collection, address: AddressSchema):
    try:
        address = await address_collection.insert_one(address)

        if address.inserted_id:
            return address

    except Exception as e:
        print(f'create_new_address.error: {e}')
        
        
      