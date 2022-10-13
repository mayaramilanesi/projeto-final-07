
from src.domain.products.models.update_product import update_product
from src.domain.products.service.service_get_product_by_code import service_get_product_by_code


async def service_update_product(product_code, product_data):
        try:
                product_dict = product_data.dict()
                
                product_searched = await service_get_product_by_code(product_code)
                if product_searched == False:
                        return False      
                updated_product = await update_product(product_code, product_dict)
                
                if updated_product == False:
                        return False
                return True
        
        except Exception as e:
                return {f'update_product_error {e}'}