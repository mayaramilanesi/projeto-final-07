# Quando avançarmos, verificar arquivo rest_conf do Ozair

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes.index import rota_principal
from src.routes.products.rota_products import rota_products
from src.routes.address.create_address import route_address



def configurar_rotas(app: FastAPI):
      app.include_router(rota_principal)
      app.include_router(rota_products)
      app.include_router(route_address)

      # app.include_router(rota_clients)
      # app.include_router(rota_cart)

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
            title="Badulaques da Lu",
            version="1.0.0"
      )
      
      
      configurar_api_rest(app)
      configurar_rotas(app)      
      return app
