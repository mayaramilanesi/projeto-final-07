from src.domain.address.models.delete_address_list import delete_address_list

async def service_delete_address_list(email):

      address_deleted = await delete_address_list(email)

      return address_deleted