"""
Este módulo conversa com Mongo para inserir, atualizar, remover
e pesquisar no MongoDB.
"""

from src.server.database_conexão_mongo import obter_colecao


NOME_COLECAO = "address"

COLECAO_ADDRESS = obter_colecao("address")


# No arquivo musicas_persistencia do Ozair tem vários exemplos de funções para trabalhar com o mongo

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

