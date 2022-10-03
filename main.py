import asyncio

from src.domain.product.controller.productController import products_crud

loop = asyncio.new_event_loop()

loop.run_until_complete(products_crud())
