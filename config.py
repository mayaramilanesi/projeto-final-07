from dotenv import load_dotenv
from pydantic import BaseSettings

# classe representando nossas configurações
class Configuracao(BaseSettings):
      database_uri = str

# Carrega as variáveis na seguinte ordem:
#1. Variáveis de ambiente
#2. Arquivo.env na raiz do projeto

def carregar_configuracoes():
      load_dotenv()
      configuracao = Configuracao()
      return configuracao