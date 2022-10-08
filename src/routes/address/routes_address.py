# Criar uma rota para cada arquivo?

from fastapi import APIRouter
from src.domain.address.service.service_get_all_address import service_find_all_address
from fastapi.encoders import jsonable_encoder


routes_address = APIRouter(
    prefix="/api/address",
    tags=["Address"]
)


@routes_address.get(
    "/", 
    summary="Pesquisar todos os endereços", 
    description="Rota para a busca de todos os endereços cadastrados",
    )
async def fetch_all_address():
    result = await service_find_all_address()
    return result


""" @routes_address.post(
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
        return {'mensagem': 'create new address failed'}  """