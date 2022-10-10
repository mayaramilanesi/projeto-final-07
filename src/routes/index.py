from fastapi import APIRouter

principal_routes = APIRouter(
    # Prefixo para o caminho da rota
    prefix="",
    #rótulo (tag) para mostrar no documento do Swagger
    tags=["Principal",],
)

@principal_routes.get( #
    "/", 
    response_model=str, # tipo de dado que vai ser informado no response
    summary="Test", #descrição que vai ao lado do verbo
    description="Main route to test server response.", # Descrição da rota
    )
async def dizer_ola():
      return "Hello Word"