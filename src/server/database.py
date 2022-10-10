from motor.motor_asyncio import AsyncIOMotorClient

class DataBase:
    client: AsyncIOMotorClient = None

    #database_uri = "DATABASE_URI"
    database_uri="mongodb+srv://mayaramilanesi:senhatlas@luizacode.egyfnn1.mongodb.net/?retryWrites=true&w=majority"

    users_collection = None
    address_collection = None
    products_collection = None
    carts_collection = None


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

    db.users_collection = db.client.luizare.users
    db.address_collection = db.client.luizare.address
    db.products_collection = db.client.luizare.products
    db.carts_collection = db.client.luizare.carts

async def disconnect_db():
    db.client.close()
