from src.server.database import db, connect_db, disconnect_db


#Função que busca usuário pelo email - acrescentar no service de criação de carrinho
async def get_user_by_email(user_email):
    await connect_db()
    users_collection = db.users_collection 
    
    try:
        user = await users_collection.find_one({'email': user_email})
           
        if user is None:
            return False
        else:
            return user
        
    except Exception:
        raise Exception("Internal error failure")  
    finally:
        	await disconnect_db()