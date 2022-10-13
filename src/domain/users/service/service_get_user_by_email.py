from src.domain.users.models.get_user_by_email import get_user_by_email

async def service_get_user_by_email(email):
    
    result = await get_user_by_email(email)
    return result