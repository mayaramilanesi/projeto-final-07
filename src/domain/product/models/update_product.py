from src.domain.schemas.product_schema import ProductUpdatedSchema
from bson.objectid import ObjectId

async def update_product(product_collection, product_id, product_data):
    try:
        data = {k: v for k, v in product_data.items() if v is not None}
        product = await product_collection.update_one(
            {'_id': ObjectId(product_id)},
            {'$set': data})
        
        if product.modified_count:
            return True
        return False, 0
    except Exception as e:
        print(f'update_product.error: {e}')
        
