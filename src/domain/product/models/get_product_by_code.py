
import pprint
from types import NoneType
async def get_product_by_code(product_collection, product_code):
    try:
        
        data = await product_collection.find_one({"code": product_code})
        if data:
            return data
        else:
            return {'message': 'Product not found'}
    except Exception as e:
        print(f'get_product.error: {e}')