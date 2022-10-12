from fastapi import APIRouter

principal_routes = APIRouter(
    prefix="",
    tags=["Principal",],
)

@principal_routes.get( 
    "/", 
    response_model=str, 
    summary="Welcome to Luizare", 
    description="Welcome to our store.", 
    )
async def dizer_ola():
      return "Hello Word"