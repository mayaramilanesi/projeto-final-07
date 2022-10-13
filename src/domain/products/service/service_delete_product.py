from src.domain.products.models.delete_product import delete_product

async def service_delete_product(product_code): 
        try:
                product = await delete_product(product_code)
                if product == True:
                        return True
                return False
        except Exception as e:
                return (f'delete_product_error {e}')
