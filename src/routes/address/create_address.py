# Criar uma rota para cada arquivo?

from fastapi import APIRouter
from src.domain.address.service.service_create_address import create_address
from src.domain.schemas.address import AddressSchema

route_address = APIRouter(
    prefix="/api/address",
    tags=["Address"]
)


@route_address.post(
    "/", 
    response_model=str, 
    summary="Criação de um novo endereço.", 
    description="Rota para a criação de um novo endereço, verificando se há ou não a existência de um usuário antes"
    )
async def create_address(address: AddressSchema):
    result = await create_address()
    
    
