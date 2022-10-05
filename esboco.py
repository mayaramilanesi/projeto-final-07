from src.domain.address.controllers.get_all_address import get_all_address
import asyncio
from src.server.database_conexão_mongo import db

      
address_collection = db.address_collection

loop = asyncio.get_event_loop()
loop.run_until_complete(get_all_address(address_collection))
