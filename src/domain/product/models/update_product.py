from src.domain.schemas.product_schema import ProductSchema, ProductUpdatedSchema
from src.server.database import db

async def update_product(product_id, product_data: ProductUpdatedSchema):
    try:
        product = product_data.dict()
        data = {k: v for k, v in product_data.items() if v is not None}
        product = await db.product_collection.update_one(
            {'_code': product_id},
            {'$set': data}
        )
        
        if product.modified_count:
            return True, product.modified_count

        return False, 0
    except Exception as e:
        print(f'update_user.error: {e}')
        
