# Criar uma rota para cada arquivo?

from fastapi import APIRouter
from src.domain.address.service.service_get_all_address import get_all_address
from src.domain.schemas.address import AddressSchema

# route_address = APIRouter(
#     prefix="/api/address",
#     tags=["Address"]
# )


# @route_address.get(
#     "/", 
#     response_model=str, 
#     summary="Pesquisar todos os endereços", 
#     description="Rota para a busca de todos os endereços cadastrados"
#     )
# async def fetch_all_address(address: AddressSchema):
#     result = await get_all_address()
#     return result