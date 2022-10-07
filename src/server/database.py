from motor.motor_asyncio import AsyncIOMotorClient

class DataBase:
    client: AsyncIOMotorClient = None
    database_uri="mongodb+srv://mayaramilanesi:senhatlas@luizacode.egyfnn1.mongodb.net/?retryWrites=true&w=majority"
    clients_collection = None
    address_collection = None
    products_collection = None
    cart_collection = None


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
    db.clients_collection = db.client.final_project.clients
    db.address_collection = db.client.final_project.address
    db.products_collection = db.client.final_project.products
    db.cart_collection = db.client.final_project.cart

async def disconnect_db():
    db.client.close()
