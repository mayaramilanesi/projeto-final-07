from pprint import pprint
from fastapi import HTTPException, status

async def get_all_products(product_collection, skip, limit):
    try:
        products_cursor = product_collection.find().skip(int(skip)).limit(int(limit))
        products = await products_cursor.to_list(length=int(limit))
        for document in products:
            pprint(document)
        
    except Exception as e:
        print(f'get_all_product.error: {e}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)