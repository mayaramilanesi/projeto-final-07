
from fastapi import APIRouter
from src.domain.schemas.user import UserSchema
from src.domain.users.service.service_create_user import service_create_user
from src.domain.users.service.service_get_user_by_email import service_get_user_by_email
from src.domain.users.service.delete_user import service_delete_user
from fastapi import HTTPException, status

routes_users = APIRouter(
    # Prefixo para o caminho da rota
    prefix="/api/users", tags=["Users"]
)


@routes_users.post("/",
    summary="Creating a new user", 
    description="Route for creating a new user, checking whether or not there are registered users via email.",
    status_code=status.HTTP_201_CREATED)          
      
async def create_user(user: UserSchema):
    result = await service_create_user(user)
    if result == True:
        return {'mensagem': 'user successfully created'}
    else:
        raise HTTPException(status_code=400, detail="The values entered do not match the required structure.")

        
@routes_users.get("/{email}",
    summary="Search user by email", 
    description="Route to search for a user through their email.",
    status_code=status.HTTP_200_OK)

async def get_user_by_email(email):
    user_searched = await service_get_user_by_email(email)
    if user_searched == False:
        return {f'message': 'User not found'}
    else:
        user_searched.pop('_id', None)
        return user_searched
    
    
@routes_users.delete("/{email}", 
    summary="Delete user by your email", 
    description="Route to delete an user by its email.",
    status_code=status.HTTP_200_OK)

async def delete_user(email):
    result = await service_delete_user(email)
    if result == True:
        return {'mensagem': 'user successfully deleted'}
    else:
        raise HTTPException(status_code=404, detail="user not found.")
    
