
from pprint import pprint
async def get_products_by_category(product_collection, product_category, skip, limit):
    try:
        products_cursor = product_collection.find({"category": product_category}).skip(int(skip)).limit(int(limit))
        products = await products_cursor.to_list(length=int(limit))
        for document in products:
            pprint(document)
    except Exception as e:
        print(f'get_products_by_category.error: {e}')       