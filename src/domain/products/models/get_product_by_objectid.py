from bson.objectid import ObjectId


async def get_product_by_objectid(product_collection, product_id):
    try:
        
        data = await product_collection.find_one(
            {"_id": ObjectId(product_id)}
        )
        if data:
            return data
        else:
            return {'message': 'Product not found'}
    except Exception as e:
        print(f'get_product.error: {e}')