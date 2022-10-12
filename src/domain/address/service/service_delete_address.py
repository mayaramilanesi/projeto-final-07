from src.domain.address.models.delete_address import delete_address

async def service_delete_address(address_id):

      address_deleted = await delete_address(address_id)

      return address_deleted
      