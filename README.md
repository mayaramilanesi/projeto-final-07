<img src="https://github.com/majhara/luizare-banco-imagens/blob/main/capa%20readme.png"> 

<h1 align="center"> L u i z a r e </h1> 

<h3 align="center"> Descrição: Repositório criado para o projeto final do bootcamp Luiza Code 5a edição, promovido pela Luiza Labs (Magalu)</h3>

<strong>1. Tecnologias utilizadas: </strong>
- Python
- Fastapi
- MongoDB


<strong>2. Bibliotecas utilizadas: </strong>
- Fastapi
- BSON
- Decimal128
- Pydantic
- Typing


<strong>3. Requisitos para execução da aplicação: </strong>
- Instalar <a href="https://www.python.org/downloads/">Python 3</a> 
- Instalar Visual Studio Code


<strong> 4. Como executar a aplicação</strong>
 - Clonar repositório
 - Copiar SSH ou HTTPS do repositório

- Na máquina local, no terminal do git execute o comando:
          <br> ```git clone + <linkdorepositório>```
- Sugere-se a criação de um ambiente virtual para isolar as dependências do projeto. Para isso, siga os passoas abaixo:
     
Dentro da pasta onde foi clonado o repositório, execute o comando no terminal
<br>        Windows: ```python -m venv + <nomedoambiente>``` </br>

- Para ativar o ambiente virtual criado, execute no terminal:
<br>       Windows: ```nomedoambiente\Scripts\activate.bat```

- Com o ambiente virtual criado e instalado, instale as dependências do projeto executando os arquivos 'requirements.txt', 'Fastapi", 'uvicorn' 'requests' e 'motor',  no terminal com os comandos:
<br> Windows: ```pip install -r requirements.txt``` - https://pypi.org/project/to-requirements.txt/
              ```pip install fastapi``` - https://pypi.org/project/fastapi/ 
              ```pip install uvicorn``` - https://pypi.org/project/uvicorn/
              ```pip install motor``` - https://pypi.org/project/motor/

- Após as dependencias do projeto instaladas execute o uvicorn para execução dos casos de testes:
<br> Windows: ```uvicorn main:app --reload```


<strong>5. Executar as aplicações:</strong>
- Acessar o Swagger pelo caminho: http://localhost:8000/docs
- Rota principal
- Post de produto
- Get de produto pelo código
- Delete de produto pelo código
- Update de produto pelo código
- Get de todos os produtos
- Get de produto por categoria
- Post de usuário
- Get de usuário por e-mail
- Delete de usuário por e-mail
- Post de endereço
- Get de todos os endereços cadastrados
- Get de endereço por e-mail do usário
- Delete do endereço pelo _id
- Post de carrinho
- Put para inserir produto pelo código no carrinho
- Get carrinho por e-mail do usuário
- Put para fechar carrinho
- Get para buscar carrinhos fechados do usuário por e-mail
- Get para buscar a quantidade de carrinhos fechados do usuário por e-mail
- Delete carrinho pelo e-mail do usuário

<strong>6. Detalhes do desenvolvimento do projeto:</strong>

## Requisitos Funcionais

* Cadastro de clientes

1. Cadastrar um cliente.
    a. Processo em que inserimos um novo cliente no sistema. - OK <br>
    b. Cada cliente precisa ter pelo menos um nome e um e-mail. - OK<br>
    c. O cliente deve informar um email válido (ao menos 3 caracteres, conter um @) - OK<br>
    d. O e-mail do cliente deve ser único, ou seja, não há dois clientes no sistema com o mesmo e-mail. - OK<br>
    e. Podemos ter dois clientes com o mesmo nome; mas, cada um com um e-mail diferente. - OK<br>
2. Cadastrar um endereço.<br>
    a. Processo de inserir um endereço para o cliente. - OK<br>
    b. Cada endereço precisa ter pelo menos um CEP, logradouro, número, cidade e estado. - OK<br>
    c. O mesmo endereço pode ser cadastrado para mais de um cliente. - OK<br>
3. Pesquisar um cliente.<br>
    a. Informado o e-mail de um cliente, apresentamos os seus dados. - OK<br>
4. Pesquisar um endereço.<br>
    a. Informando o e-mail de um cliente, apresentamos seus endereços. - OK <br>
5. Remover um cliente. (Opcional)<br>
    a. Remover um cliente pode remover também os endereços relacionados. - OK<br>
    b. Ao remover um cliente remover também carrinho aberto. - OK<br>
6. Remover um endereço. (Opcional)<br>
    a. Com base em alguma chave, por exemplo, é possível remover o endereço do cliente. - OK<br>

* Gerenciamento de produtos<br>

1. Cadastrar um produto.<br>
    a. Processo em que registra-se um novo produto no sistema. - OK<br>
    b. Cada produto precisa ter pelo menos um nome, uma descrição e um código único. - OK<br>
    c. Um produto pode ter um preço de venda, que é um valor superior a R$ 0,01. - OK<br>
    d. Um produto pode ter um valor de estoque, que é um valor superior a 0. - OK<br>
    e. O código do produto informado no processo de cadastro deve ser único, ou seja, não há dois produtos no sistema com o mesmo código. - OK<br>
    f. Os nomes dos produtos podem ser únicos. - OK<br>
    g. Campos adicionais podem ser informados conforme a categoria do seu projeto. - OK<br>
2. Atualizar os dados de um produto.<br>
    a. Poderemos atualizar os dados de um produto com base no seu código. - OK<br>
    b. O código do produto não pode ser alterado [PRÓXIMA IMPLEMENTAÇÃO]
    c. O nome do produto pode ser alterado. - OK<br>
    d. Quaisquer outros campos do produto que existam em seu projeto poderão ser atualizados. - OK<br>
3. Pesquisar um produto. <br>
    a. Informado o código do produto, apresentamos os seus dados. - OK<br>
4. Pesquisar um produto pelo nome.<br>
    a. Informe um texto para o nome do produto, então iremos pesquisar pelos produtos que contenham o nome informado.<br>
5. Remover um produto. (Opcional)<br>
    a. Poderemos remover um produto com base em seu código. - OK<br>
    b. Atentar neste caso: Este produto está em algum carrinho de compras? O que fazer? O seu grupo irá decidir.<br>

* Carrinho de compras

1. Abertos: Cada cliente pode ter apenas um carrinho de compras aberto na aplicação. - OK<br>
2. Fechados: São os carrinhos de compras os quais a compra já foi fechada. - OK<br>
Solicitamos o seguinte:<br>
1. Criar um carrinho de compras aberto e adicionar itens ao carrinho.<br>
    a. Todo carrinho de compras deve conter um cliente. - OK<br>
    b. É opcional, ter um produto inicialmente. [Em nossa implementação, o carrinho é criado vazio] <br>
    c. Se há um produto um mais produtos, na criação do carrinho, informe a quantidade de cada produto. No seu trabalho, você pode começar com apenas um produto. - OK <br>
    d. Ao criar o carrinho, você deve:<br>
        i. Validar se o cliente existe - OK<br>
        ii. Validar se o produto a ser adicionado no carrinho existe - OK<br>
        iii. Verificar se o cliente já possui um carrinho aberto. Caso contrário criar um carrinho novo. - OK<br>
        iv. Validar se a quantidade de itens do produto a ser adicionado no carrinho está disponível no estoque (opcional). OK<br>
    e. Ao adicionar um item no carrinho, o mesmo terá o valor total e quantidade de itens atualizado - OK<br>
2. Alterar a quantidade de itens do carrinho novo.<br>
    a. No carrinho novo, com base no produto informado, a quantidade é modificada.<br>
    b. Para isto:<br>
        i. Validar se produto existe no carrinho - OK<br>
        ii. Validar se existe estoque para a quantidade desejada do produto (opcional). - OK<br>
        iii. Atualizar o valor total e quantidade de itens do carrinho - OK<br>
    c. Se o carrinho zerar o número de itens, ou seja, o cliente removeu todos os itens do carrinho, o mesmo pode ser excluído. - Não foi feito<br>
3. Consultar carrinho de compras aberto:<br>
    a. Informar o cliente e retornar os dados do carrinho e produtos - OK<br>
4. Consultar os carrinhos fechados de um cliente (opcional). - OK<br>
5. Consultar os produtos e suas quantidades em carrinhos fechados (opcional). - OK<br>
6. Consultar quantos carrinhos fechados os clientes possuem (opcional). - OK<br>
7. Fechar o carrinho aberto:<br>
    a. Simplesmente pode-se mudar o tipo do carrinho de compras para “fechado”. - OK<br>
    b. Opcionalmente, o grupo pode adicionar o seguinte:<br>
        i. Identificar o endereço do cliente que será utilizado como o de entrega. - OK<br>
        ii. Validar se o estoque pedido dos itens ainda está disponível, se estiver reduzir do estoque dos produtos a quantidade de itens do produto no carrinho (Muito opcional). - Não foi feito <br>
        iii. Associar um identificador ao carrinho de compras como sendo o número do pedido. <br>
8. Excluir carrinho do cliente (opcional) - OK
    a. Quer o carrinho seja aberto ou fechado, podemos remover o carrinho do sistema. - OK

* Entregas extras realizadas
- Documentar a API Rest com o Swagger/OpenAPI ou RedDoc. - OK
- Organizar e estruturar o código do projeto. - OK
- Montar um arquivo README.md detalhando o projeto. - OK

* Próximas implementações:
- Criação de testes unitários
- A API poderá utilizar algum recurso de autorização e autenticação
- O projeto poderá gerar mensagens de log ou utilizar mecanismos de logging
- Realizar o deploy da aplicação
- Hospedagem em alguma plataforma como o Heroku e/ou ainda ter um arquivo Dockerfile ou docker-compose que ajude em seu futuro deploy/teste


<table><strong>Desenvolvido por: </strong><br>
<tr><td>Mayara Milanesi</td><td><a href="https://www.linkedin.com/in/mayara-milanesi-b114b2161/">LinkedIn</a></td><td><a href="https://github.com/mayaramilanesi">GitHub</a></td></tr>
<tr><td>Mayara Simões</td><td><a href="https://www.linkedin.com/in/mayara-simoes">LinkedIn</a></td><td><a href="https://github.com/majhara">GitHub</a></td></tr>
<tr><td>Renata Perez</td><td><a href=""> LinkedIn </a></td><td><a href="https://github.com/Renata-Perez">GitHub</a></td></tr></table>
   
     
   

