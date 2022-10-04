
from unicodedata import category
from src.domain.product.models.get_all_products import get_all_products
from src.domain.product.models.get_product_by_name import get_product_by_name
from src.domain.product.models.create_product import create_product
from src.domain.product.models.delete_product import delete_product
from src.domain.product.models.update_product import update_product
from src.domain.product.models.get_product_by_objectid import get_product_by_objectid
from src.domain.product.models.get_products_by_category import get_products_by_category
from src.domain.product.models.get_product_by_code import get_product_by_code
from src.server.database import connect_db, db, disconnect_db



db_product = {}

async def products_crud():
    option = input("Digite a opção de CRUD: \n1 - Criar produto |  2 - Buscar produto pelo código | 3 - Buscar produto pelo nome | 4 - Atualizar produto | 5 - Deletar produto  | 6 - Buscar todos os produtos\n")
    await connect_db()
    product_collection = db.product_collection
    
    product = {}
    
    #Create product
    if option == '1':
        product["name"] = input("Nome do produto: ")
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
        return product_found
                
    #update product
    elif option == '4':
        product_id = input("Digite o ObjectId do produto a atualizar: ")
        product_searched = await get_product_by_objectid(product_collection, product_id)

        product_data = {"description": "New description",
                        "Price": 45.99
                        }

        is_updated = await update_product(product_collection, product_id, product_data)
        if is_updated:
            print(f"Atualização realizada com sucesso")
        else:
            print("Atualização falhou!")  

    
    # delete product
    elif option == '5':
    
        product["_id"] = input("Digite o ObjectId do produto a ser deletado: ")
        product_found = await get_product_by_objectid(product_collection, product["_id"])
        
        result = await delete_product(product_collection, product_found["_id"])
        print(result)
    
    elif option == '6':
        
        products = await get_all_products(product_collection, skip=0, limit=2)
        print(products)
        
    elif option == '7':
        product["_id"] = input("Digite o ObjectId do product a ser buscado: ")
        product_searched = await get_product_by_objectid(product_collection, product["_id"])
        print(product_searched)
        
    #get all products by category
    elif option == '8':
        product["category"] = input("Digite a categoria a ser buscada: ")
        await get_products_by_category(product_collection, product["category"], skip=0, limit=2)

        
        
    await disconnect_db()