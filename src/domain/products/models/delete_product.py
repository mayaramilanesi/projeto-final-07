from bson.objectid import ObjectId

async def delete_product(product_collection, product_id):
    try:
        product = await product_collection.delete_one({"_id": ObjectId(product_id)})
        if product.deleted_count:
            return {'status': 'Product deleted'}
    except Exception as e:
        print(f'delete_user.error: {e}')
