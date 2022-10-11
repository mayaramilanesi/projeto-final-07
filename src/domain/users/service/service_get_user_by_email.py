
from src.domain.users.models.get_user_by_email import get_user_by_email



async def service_get_user_by_email(user_email):
    try: 
        result = await get_user_by_email(user_email)
        if result:
            return result
        return False
    
    except Exception as e:
        return {f'get_user_by_email_error {e}'}