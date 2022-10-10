
from fastapi import APIRouter
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

async def create_new_product(product: ProductSchema):
    result = await service_create_new_product(product)
    if result == True:
        return {"message": "product successfully created"}
    else:
        raise HTTPException(status_code=409, detail="A product with the same name or code already exists")
  
        
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

    
@routes_products.put("/{codigo}")
async def update_product(product: ProductUpdatedSchema):
   result = await service_update_product(product)
   return result   

    
@routes_products.get("/", summary="Getting all products",
                    description="This route will return a list of all products")
async def find_all_products():
    result = await service_get_all_products()
    if result == False:
        raise HTTPException
    return result


@routes_products.get("/category/{category}")

async def get_products_by_category(category: str):
    result = await service_get_product_by_category(category)
    if result == False:
        raise HTTPException(status_code=404, description="Category not found")
    return result



@routes_products.delete("/{codigo}")
async def delete_product(product_code):
    result = await service_delete_product(product_code)
    if result == False:
        raise HTTPException(status_code=404, description="Product not found")
    return {"message": "product successfully deleted"}