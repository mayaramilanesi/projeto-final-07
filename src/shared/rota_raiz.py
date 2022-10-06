from fastapi import FastAPI

app = FastAPI()


#Root
@app.get("/")
async def root():
    return {
        "message": "Welcome to our application!"
    }
