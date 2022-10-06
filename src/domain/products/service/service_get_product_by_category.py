from src.domain.products.models.get_products_by_category import get_products_by_category


#Ainda não está ajustado de acordo com a arquitetura e regras que definimos
async def service_get_product_by_category(product_collection, product_category):
    products_list = []
    products = await get_products_by_category(product_collection, product_category)
    if products is not None:
        products_list.append(products)
        return products_list
    else:
        return {'message': 'No products found for category'}
