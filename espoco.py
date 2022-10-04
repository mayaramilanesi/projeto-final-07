from src.server.acessar_bd import pesquisar_todos_os_enderecos, pesquisar_pelo_codigo
import asyncio

async def testar():
      lista = await pesquisar_pelo_codigo()
      print(lista)
      

#asyncio.run(testar())
asyncio.get_event_loop().run_ultil_complete