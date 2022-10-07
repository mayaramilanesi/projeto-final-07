
from fastapi import APIRouter

from domain.schemas.user import ClientSchema
from src.domain.users.service import service_create_user, service_get_user_by_email

routes_users = APIRouter(
    # Prefixo para o caminho da rota
    prefix="/api/users", tags=["Users"]
)


@routes_users.post("/user")
async def create_user(user: ClientSchema):
    result = await service_create_user(user)
    if result == True:
        return {'mensagem': 'user successfully created'}
    else:
        return {'mensagem': 'create user failed'}

        
@routes_users.get("/{email}")
async def get_user_by_email(email: str):
    user_searched = await service_get_user_by_email(email)
    if user_searched == False:
        return {f'message': 'User not found'}
    else:
        return user_searched