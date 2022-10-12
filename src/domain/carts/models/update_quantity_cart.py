from src.server.database import db, connect_db, disconnect_db
 

async def update_quantity_cart(cart):
    try: 
        await connect_db()
        
        carts_collection = db.carts_collection
        
        filter = { 'user_email' : cart['user_email'], 'opened': True}
        new_value ={
                    '$set': {   "total_price": cart["total_price"],
                                "total_quantity": cart["total_quantity"]
                            }
                    }
        cart = await carts_collection.update_one(filter, new_value)

        if cart:
            return True
        else:
            return False
        
    except Exception as e:
        print(f'insert_product_to_cart.error: {e}')
    finally:
        await disconnect_db()