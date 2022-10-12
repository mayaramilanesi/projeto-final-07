from src.domain.users.models.get_user_by_email import get_user_by_email
from src.domain.users.models.create_user import create_user
from src.domain.schemas.user import UserSchema


async def service_create_user(user: UserSchema):
    
    data_user = await get_user_by_email(user.email)
    
    if data_user == False:
        result = await create_user(user.dict())
        return result
    return False