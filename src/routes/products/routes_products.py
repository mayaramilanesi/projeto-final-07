
from fastapi import APIRouter, Body
from fastapi import HTTPException, status
from src.domain.schemas.product import ProductSchema, ProductUpdatedSchema
from src.domain.products.service.service_get_product_by_code import service_get_product_by_code
from src.domain.products.service.service_create_new_product import service_create_new_product
from src.domain.products.service.service_get_product_by_category import service_get_product_by_category
from src.domain.products.service.service_update_product import service_update_product
from src.domain.products.service.service_get_all_products import service_get_all_products
from src.domain.products.service.service_delete_product import service_delete_product

routes_products = APIRouter(
    prefix="/api/products", tags=["Products"]
)


@routes_products.post("/new", 
                    summary="Inserting a new product",
                    description="This route will be executed when the product is added to the list of products",
                    status_code=status.HTTP_201_CREATED)

async def create_new_product(product: ProductSchema = Body(
        example={
            "name": "The entire name of the new product",
            "description": "a brief description of the product",
            "price": "A value greater than 0.01",
            "image": "a URL to the product image",
            "code": "Product bar code",
            "category": "Product category: Choose among the following categories: jewelry, semi-jewel or costume jewelry",
            "inventory": "A integer number - product in stock",
            }
        )
    
    ):
    result = await service_create_new_product(product)
    if result['status'] == False:
        raise HTTPException(status_code=422, detail=result['message'])
    return {"product successfully created"}

        
  
        
@routes_products.get("/{code}",
                    summary="Getting a product by its code",
                    description="This route will return a product by its code",
                    status_code=status.HTTP_200_OK)
async def get_product_by_code(code: str):
    product_searched = await service_get_product_by_code(code)
    if product_searched == False:
        raise HTTPException(status_code=404, detail="Product not found")
    else:
        return product_searched

    
@routes_products.put("/update/{code}")
async def update_product(product_code, product: ProductUpdatedSchema=Body(
    example={
            "name": "A new name for the product (Optional)",
            "description": "a brief description of the product (Optional)",
            "price": "A value greater than 0.01 (Optional)",
            "image": "a URL to the product image (Optional)",
            "category": "Product category: Choose among the following categories: jewelry, semi-jewel or costume jewelry (Optional)"})):
   result = await service_update_product(product_code, product)
   if result == False:
       raise HTTPException(status_code=409, detail="Product not found. Change product code and try again")
   return {'message': 'Product updated successfully'}  

    
@routes_products.get("/", summary="Getting all products",
                    description="This route will return a list of all products")

async def find_all_products():
    result = await service_get_all_products()
    if result == False:
        raise HTTPException(status_code=404, detail="No products found")
    return result


@routes_products.get("/category/{category}")
async def get_products_by_category(category: str):
    result = await service_get_product_by_category(category)
    if result == False:
        raise HTTPException(status_code=404, detail="Category not found")
    return result



@routes_products.delete("/{code}")
async def delete_product(product_code):
    result = await service_delete_product(product_code)
    if result == False:
        raise HTTPException(status_code=404, description="Product not found")
    return {"message": "product successfully deleted"}