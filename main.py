from src.server.rest_conf import criar_aplicacao_fastapi


# Criando minha aplicação FastAPI e deixando-a 'global'.
# Este `app` será 'chamado' pelo uvicorn. 
app = criar_aplicacao_fastapi()

