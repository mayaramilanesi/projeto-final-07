import src.server.acessar_bd as bd_persistencia

# Arquivo para fazer as validações de pesquisa

async def pesquisar_todos():
      lista = await bd_persistencia.pesquisar_todos_os_enderecos()
      return lista

async def pesquisar_pelo_codigo(codigo: str):
      address = await bd_persistencia.pesquisar_pelo_codigo(codigo)
      return address