from __future__ import annotations

from ctypes import Union
from enum import Enum
from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Annotated

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"



class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

srv = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}, {"item_name": "ars"}]

@srv.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}

@srv.post("/items/")
async def create_item(item: Item):

    return item

@srv.get("/items/")
async def read_item(q: Annotated[str | None, Query(max_length=50)] = None, skip: int = 0, limit: int = 10):
    results = fake_items_db[skip: skip + limit]
    if q:
        results.append({"item_name": "q = " + q})
    return results

@srv.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}

@srv.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@srv.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item