from domain.address.models.acessar_bd import pesquisar_todos_os_enderecos
import asyncio

async def testar():
      lista = await pesquisar_todos_os_enderecos()
      print(lista)
      

#asyncio.run(testar())
asyncio.get_event_loop().run_ultil_complete