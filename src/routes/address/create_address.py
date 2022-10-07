# Criar uma rota para cada arquivo?

from fastapi import APIRouter
from src.domain.address.service.service_create_address import service_create_address 
from src.domain.address.service.service_get_all_address import service_get_all_address
from src.domain.schemas.address import AddressSchema, Address

# route_address = APIRouter(
#     prefix="/api/address",
#     tags=["Address"]
# )


@route_address.post(
    "/", 
    response_model=dict, 
    summary="Criação de um novo endereço.", 
    description="Rota para a criação de um novo endereço, verificando se há ou não a existência de um usuário antes"
    )
async def create_address(address: AddressSchema, email):
    
    result = await service_create_address(address, email)
    
    if result == True:
        return {'mensagem': 'address successfully created'}
    else:
        return {'mensagem': 'create new address failed'} 
    


@route_address.get(
    "/", 
    response_model=list, 
    summary="Buscando todos os endereços.", 
    description="Rota para a busca de uma lista com todos os endereços cadastrados"
    )
async def fetch_all_address():
    
    result = await service_get_all_address()
    
    if result == True:
        return {'mensagem': 'address search success'}
    else:
        return {'mensagem': 'address lookup failed'} 
    
    
