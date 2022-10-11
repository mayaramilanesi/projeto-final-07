from src.domain.users.models.delete_user import delete_user


async def service_delete_user(email): 
      
      user_deleted = await delete_user(email)
      
      return user_deleted
            
