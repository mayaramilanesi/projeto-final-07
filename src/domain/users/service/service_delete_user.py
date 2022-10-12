from src.domain.users.models.delete_user import delete_user
from src.domain.address.service.service_delete_address_list import service_delete_address_list
from src.domain.carts.service.service_delete_all_carts import service_delete_all_carts


async def service_delete_user(email):     
      
      user_deleted = await delete_user(email)
      
      if user_deleted:
            await service_delete_address_list(email)
            await service_delete_all_carts(email)
            
            return user_deleted
            
