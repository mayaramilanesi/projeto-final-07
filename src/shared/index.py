
from fastapi import FastAPI

app = FastAPI()


#Root
@app.get("/")
async def root():
    return "Seja bem-vindo(a)"



#Creating a product
@app.post("/")
async def insert_product():
    ...

@app.get("/produto/{code}/")
async def get_product_by_code():
    ...
    
    
#Updating a product
@app.put("/")
async def update_product():
    ...
    
#Deleting a product   
@app.delete("/produto/{code}/")
async def delete_product():
    ...