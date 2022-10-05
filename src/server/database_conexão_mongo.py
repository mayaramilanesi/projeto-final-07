# Configurações de conexão com o Mongo


import asyncio

from motor.motor_asyncio import AsyncIOMotorClient

from config_dotenv import configuracao

""" def iniciar_cliente_mongo() -> AsyncIOMotorClient:
    
    cliente_mongo = AsyncIOMotorClient(configuracao.database_uri)
    cliente_mongo.get_io_loop = asyncio.get_event_loop
    return cliente_mongo

# Meu cliente 'global' para o mongodb
cliente_mongo = iniciar_cliente_mongo()


# ---------------------------------------------------
# Funções auxiliares para quem for trabalhar com
# a persistência.
# ---------------------------------------------------

def obter_base_dados() -> AsyncIOMotorDatabase:
    # Obtém a base de dados (database) padrão
    # (a que está na string de conexão)
    return cliente_mongo.get_default_database()


def obter_colecao(nome_colecao: str) -> AsyncIOMotorCollection:
    # Obtém a coleção informada da base de dados padrão.
    bd = obter_base_dados()
    colecao = bd[nome_colecao]

    return colecao """
    
    
    
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