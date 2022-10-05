# Configurações de conexão com o Mongo


import asyncio

from motor.motor_asyncio import AsyncIOMotorClient

from config_dotenv import configuracao

    
    
    
class DataBase:
    client: AsyncIOMotorClient = None
    database_uri = configuracao.database_uri
    clients_collection = None # VARIÁVEIS PARA ACESSAR AS COLEÇÕES
    address_collection = None
    products_collection = None 
    cart_collection = None
  

db = DataBase()

async def connect_db(): # CONEXÃO COM O BANCO
    # conexao mongo, com no máximo 10 conexões async
    db.client = AsyncIOMotorClient(
        db.database_uri,
        maxPoolSize=10, # QUANTIDADE DE CONEXÕES ASSINCRONAS QUE VOU PERMITIR
        minPoolSize=10,
        tls=True,
        tlsAllowInvalidCertificates=True,
        
    )
    db.clients_collection = db.client.final_project.clients # CHAMANDO AS COLEÇÕES
    db.address_collection = db.client.final_project.address
    db.products_collection = db.client.final_project.products
    db.cart_collection = db.client.final_project.cart

async def disconnect_db(): # FECHAR CONEXÃO COM O BANCO
    db.client.close()