from os import environ
from motor.motor_asyncio import AsyncIOMotorClient

class DataBase:
    client: AsyncIOMotorClient = None
    database_uri = 'DATABASE_URI'
    users_collection = None
    address_collection = None
    product_collection = None
    order_collection = None
    order_items_collection = None

db = DataBase()

async def connect_db():
    # conexao mongo, com no máximo 10 conexões async
    db.client = AsyncIOMotorClient(
        db.database_uri,
        maxPoolSize=20,
        minPoolSize=20,
        tls=True,
        tlsAllowInvalidCertificates=True
    )
    db.users_collection = db.client.test.users
    db.address_collection = db.client.teste.address
    db.product_collection = db.client.teste.products
    db.order_collection = db.client.teste.orders
    db.order_items_collection = db.client.teste.order_items

async def disconnect_db():
    db.client.close()
