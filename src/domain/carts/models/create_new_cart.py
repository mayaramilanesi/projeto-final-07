from itertools import product
from re import U
from bson.objectid import ObjectId
from src.domain.schemas.user import UserSchema

async def create_open_order(carts_collection, user_id):
    opened_order = await get_opened_order_by_user_id(carts_collection, user_id)
    if opened_order is None:
        order = {
            "user_id": user_id,
            "products": [],
            "total_order": 0.00,
            "opened": True
        }
        
        opened_order = await create_order(carts_collection, order)
    return opened_order
            

async def create_order(carts_collection, order):
    try:
        order = await carts_collection.insert_one(order)

        if order.inserted_id:
            order = await get_order(carts_collection, order.inserted_id)
            return order

    except Exception as e:
        print(f'create_order.error: {e}')

async def get_order(carts_collection, order_id):
    try:
        order = await carts_collection.find_one({'_id': order_id})
        if order:
            return order
    except Exception as e:
        print(f'get_order.error: {e}')
        return None


async def get_opened_order_by_user_id(carts_collection, user_id):
    try:
        order = await carts_collection.find_one({'user_id': user_id, 'opened': True})
        if order:
            return order
    except Exception as e:
        print(f'get_order.error: {e}')

async def validate_order_by_email_user(carts_collection, email):
	try:
		order_cursor =  carts_collection.aggregate([
			{
				"$match":{ "user.email": email}
			}
		])
		return await order_cursor.to_list(1)

	except Exception as e:
		print(f'get_address.error: {e}')
  
product = {
    "id_product": ObjectId("632f899f21f055930b9f3dff"),
    "price": 899.00,
    "quantity": 1,
    "total": 0.00
}

list_product = [list]  

def insert_products_in_list(product: dict):
    list_product.append(product)
    return list_product

def isolar_produto(order):
    order = get_order
    order.product = [product]
    return order
  
async def insert_product_in_order(carts_collection, products: dict, opened_order):
    # Filtro de atualização
    filter = {
        "_id": opened_order._id
    }
    # Registro no 'formato MongoDB' para atualizar.
    update_product = {
        "$set":{
            "products": products,
        }
    }
    order = await carts_collection.update_one(filter, update_product)
  
    return order


async def closed_order(carts_collection, opened):
    filter = {
        opened: True
    }
    updated_record = {
        "$set": False
    }
    order = await carts_collection.update_one(filter, updated_record)
    return order
     
        
async def delete_order(carts_collection, order_id):
    try:
        order = await carts_collection.delete_one(
            {'_id': order_id}
        )
        if order.deleted_count:
            return {'status': 'Order deleted'}
    except Exception as e:
        print(f'delete_order.error: {e}')
