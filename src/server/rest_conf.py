# Quando avançarmos, verificar arquivo rest_conf do Ozair

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

<<<<<<< HEAD
from src.routes.index import principal_routes
from src.routes.products.rota_products import routes_products
=======
from src.routes.index import routes_principal

from src.routes.products.routes_products import routes_products
>>>>>>> 40ea08affc4bea610ec73a47fc47dafd363e9681
from src.routes.address.routes_address import routes_address
from src.routes.users.routes_users import routes_users


def configurar_rotas(app: FastAPI):
      app.include_router(principal_routes)
      app.include_router(routes_products)
      app.include_router(routes_address)
      app.include_router(routes_users)
      
      
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
            title="Luizare",
            version="1.0.0"
      )
      
      
      configurar_api_rest(app)
      configurar_rotas(app)      
      return app
