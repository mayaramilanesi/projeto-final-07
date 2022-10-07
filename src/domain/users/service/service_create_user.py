from src.domain.users.models.create_user import create_user
from src.domain.schemas.user import UserSchema



async def service_create_new_product(product: UserSchema):
    user_dict = user_dict.dict()
    #Validacoes de Produto....
    result = await create_user(user_dict)
    return result
