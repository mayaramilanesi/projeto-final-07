
from fastapi import HTTPException, status


async def get_all_products(product_collection):
    try:
        products_cursor = product_collection.find_many()
        products_list = await products_cursor.to_list()
        return products_list
    except Exception as e:
        print(f'get_all_product.error: {e}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)