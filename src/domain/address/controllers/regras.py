"""
Regras e ajustes para músicas. Aqui devem estar todas as regras para de validação de entrada, saída e atualização do bd. Essas funções serão chamadas nas rotas. Ver exemplos no arquivo musicas_regras do Ozair
"""

import domain.address.models.acessar_bd as bd_persistencia

# Arquivo para fazer as validações de pesquisa

async def pesquisar_todos():
      lista = await bd_persistencia.pesquisar_todos_os_enderecos()
      return lista

async def pesquisar_pelo_codigo(codigo: str):
      address = await bd_persistencia.pesquisar_pelo_codigo(codigo)
      return address