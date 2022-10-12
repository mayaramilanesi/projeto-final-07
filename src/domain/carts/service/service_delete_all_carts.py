from src.domain.carts.models.delete_all_carts import delete_all_carts


async def service_delete_all_carts(email): 
      
      cart_deleted = await delete_all_carts(email)

      return cart_deleted