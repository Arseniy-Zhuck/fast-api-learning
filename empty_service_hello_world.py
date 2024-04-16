from fastapi import FastAPI

srv = FastAPI()

@srv.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@srv.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}