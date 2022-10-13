from src.server.database import db, connect_db, disconnect_db
 
async def delete_product_from_cart(cart, product_code):
    try: 
        await connect_db()
        
        carts_collection = db.carts_collection
        
        filter = { 'user_email' : cart['user_email'], 'opened': True}
        #new_value = { '$pull': {"products": product_code}}
        new_value = { '$set': {"products": cart['products']}}
        
        new_product = await carts_collection.update_one(filter, new_value)

        if new_product:
            return True
        else:
            return False
        
    except Exception as e:
        print(f'delete_product_from_cart.error: {e}')
    finally:
        await disconnect_db()