from src.server.database import (conectar_cliente_mongo, acessar_colecao)


NOME_COLECAO = "address"

COLECAO_ADDRESS = acessar_colecao(conectar_cliente_mongo(), NOME_COLECAO)

async def pesquisar_todos_os_enderecos():
      lista_enderecos = []
      filtro = {}
      cursor = COLECAO_ADDRESS.find(filtro)
      address = await cursor.to_list()
      async for a in address:
            lista_enderecos.append(a)
      return lista_enderecos


async def pesquisar_pelo_codigo(codigo):
      filtro = {"codigo": codigo}
      address = await COLECAO_ADDRESS.find_one(filtro)
      return address

