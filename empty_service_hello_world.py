from fastapi import FastAPI

srv = FastAPI()

@srv.get("/")
async def root():
    return {"message" : "Hello, World!"}

