# Criar uma rota para cada arquivo?

from fastapi import APIRouter
import src.domain.address.controllers.regras as regras

rota_address = APIRouter(
    # Prefixo para o caminho da rota
    prefix="/api/address"
)


@rota_address.post("/")
async def criar_novo_endereco(endereco: dict):
    print("Salvar novo endereço, endereco")
    return {
        "endereco": endereco
    }
    
    
@rota_address.get("/{codigo}")
async def pesquisar_address_pelo_codigo(codigo: str):
    print("Pesquisar pelo codigo", codigo)
    address = await regras.pesquisar_pelo_codigo()
    return address
    
    
    
@rota_address.get("/")
async def pesquisar_todos_enderecos():
    print("Pesquisar todos os endereços")
    lista = await regras.pesquisar_todos()
    return lista
