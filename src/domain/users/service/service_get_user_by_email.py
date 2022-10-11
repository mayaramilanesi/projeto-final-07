from src.domain.users.models.get_user_by_email import get_user_by_email
from src.util.service import format_json

async def service_get_user_by_email(email):
    
    result = await get_user_by_email(email)
    return result




# async def service_find_all_address():
      
#       result =  await format_json(await get_all_address())
      
#       return result
