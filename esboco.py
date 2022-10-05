from src.domain.address.models.get_address_by_email import delete_address
import asyncio

async def testar():
      lista = await delete_address()
      print(lista)
      

#asyncio.run(testar())
asyncio.get_event_loop().run_ultil_complete