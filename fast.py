from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def real_root():
    return{"message": "Hello World"}