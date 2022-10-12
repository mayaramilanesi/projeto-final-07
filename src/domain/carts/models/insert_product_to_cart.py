from src.server.database import db, connect_db, disconnect_db
 

async def insert_product_to_cart(cart, product):
    try: 
        await connect_db()
        
        carts_collection = db.carts_collection
        
        product = product.dict()
        filter = { 'user_email' : cart['user_email'], 'opened': True}
        new_value = { '$push': {"products": product}}
        new_product = await carts_collection.update_one(filter, new_value)

        if new_product:
            return True
        else:
            return False
        
    except Exception as e:
        print(f'insert_product_to_cart.error: {e}')
    finally:
        await disconnect_db()