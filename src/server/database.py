from motor.motor_asyncio import AsyncIOMotorClient


class DataBase:
    client: AsyncIOMotorClient = None
    database_uri = "mongodb+srv://mayaramilanesi:4623nick@luizacode.egyfnn1.mongodb.net/?retryWrites=true&w=majority"
    clients_collection = None 
    address_collection = None
    product_collection = None
    order_collection = None
    order_items_collection = None

db = DataBase()

async def connect_db(): 
    db.client = AsyncIOMotorClient(
        db.database_uri,
        maxPoolSize=10, 
        minPoolSize=10,
        tls=True,
        tlsAllowInvalidCertificates=True
    )
    db.clients_collection = db.client.shopping_cart.clients 
    db.address_collection = db.client.shopping_cart.address
    db.product_collection = db.client.shopping_cart.products
    db.order_collection = db.client.shopping_cart.orders
    db.order_items_collection = db.client.shopping_cart.order_items

async def disconnect_db(): # FECHAR CONEXÃO COM O BANCO
    db.client.close()