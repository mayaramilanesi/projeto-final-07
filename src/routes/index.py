from fastapi import APIRouter

<<<<<<< HEAD
principal_routes = APIRouter(
=======
routes_principal = APIRouter(
>>>>>>> 40ea08affc4bea610ec73a47fc47dafd363e9681
    # Prefixo para o caminho da rota
    prefix="",
    #rótulo (tag) para mostrar no documento do Swagger
    tags=["Principal",],
)

<<<<<<< HEAD
@principal_routes.get( #
=======
@routes_principal.get( #
>>>>>>> 40ea08affc4bea610ec73a47fc47dafd363e9681
    "/", 
    response_model=str, # tipo de dado que vai ser informado no response
    summary="Diga oi.", #descrição que vai ao lado do verbo
    description="Rota principal em que se diz um Oi.", # Descrição da rota
    )
async def dizer_ola():
      return "Hello Word"