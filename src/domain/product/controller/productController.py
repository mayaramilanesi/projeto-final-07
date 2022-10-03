
from src.domain.product.models.get_product_by_name import get_product_by_name
from src.domain.product.models.create_product import create_product
from src.domain.product.models.delete_product import delete_product
from src.domain.product.models.get_product_by_code import get_product_by_code
from src.server.database import connect_db, db, disconnect_db



db_product = {}

async def products_crud():
    option = input("Digite a opção de CRUD: \n1 - Criar produto |  2 - Buscar produto pelo código | 3 - Buscar produto pelo nome | 4 - Atualizar produto | 5 - Deletar produto\n")
    await connect_db()
    product_collection = db.product_collection
    
    product = {}
    
    #Create product
    if option == '1':
        product["name"] = input("Nome do produto:  ")
        product["description"] = input("Descrição do produto: ")
        product["price"] = float(input("Preço: "))
        product["category"] = input("Category: ")
        product["inventory"] = int(input("Inventory: "))
        product["code"] = input("Code: ")
        # create user
        new_product = await create_product(product_collection, product)
        print(new_product)
           
    # get product by code
    elif option == '2':
        product["code"] = input("Digite o código do produto: ")        
        product_found = await get_product_by_code(product_collection, product["code"])
        print(product_found)
                    
    # get product by name
    elif option == '3':
        
        product["name"] = input("Digite o nome do produto: ")        
    
        product_found = await get_product_by_name(product_collection, product["name"])
        print(product_found)
                
    #update product
    elif option == '4':
        ...  

    
    # delete product
    elif option == '5':
    
        product['code'] = input("Digite o código do produto a ser deletado: ")
        product_found = await get_product_by_code(product_collection, product['code'])
        
        result = await delete_product(product_collection, product['code'])
        return result
    
        
    await disconnect_db()