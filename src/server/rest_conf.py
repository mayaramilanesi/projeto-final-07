# Quando avançarmos, verificar arquivo rest_conf do Ozair

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.shared.routes.index import rota_principal
""" from src.shared.routes.address import rota_address
from src.shared.routes.clients import rota_clients
from src.shared.routes.products import rota_products
from src.shared.routes.cart import rota_cart """

def configurar_rotas(app: FastAPI):
      app.include_router(rota_principal)
"""       app.include_router(rota_address)
      app.include_router(rota_clients)
      app.include_router(rota_products)
      app.include_router(rota_cart) """

def configurar_api_rest(app: FastAPI):
      app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
)



def criar_aplicacao_fastapi():
      app = FastAPI(
            title="Loja de Joias e Bijouterias",
            version="01"
      )
      
      
      configurar_api_rest(app)
      configurar_rotas(app)      
      return app
