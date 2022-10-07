from fastapi import APIRouter

routes_principal = APIRouter(
    # Prefixo para o caminho da rota
    prefix="",
    #rótulo (tag) para mostrar no documento do Swagger
    tags=["Principal",],
)

@routes_principal.get( #
    "/", 
    response_model=str, # tipo de dado que vai ser informado no response
    summary="Diga oi.", #descrição que vai ao lado do verbo
    description="Rota principal em que se diz um Oi.", # Descrição da rota
    )
async def dizer_ola():
      return "Hello Word"