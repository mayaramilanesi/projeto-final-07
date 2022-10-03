import asyncio

from src.controllers.address import address_crud


loop = asyncio.get_event_loop()
loop.run_until_complete(address_crud())