

async def get_all_address(address_collection):
      try:
            address = await address_collection.find({})

            if address:
                  return address

      except Exception as e:
            print(f'find_address.error: {e}')