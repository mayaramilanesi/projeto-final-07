
 
async def get_product_by_name(product_collection, product_name):
    try:
        data = await product_collection.find_one({'name': product_name})
        if data:
            return data
        else:
            return {'message_returned': 'Product not found'}
    except Exception as e:
        print(f'get_product.error: {e}')