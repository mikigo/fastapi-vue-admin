import os
from typing import Union

import uvicorn
from pydantic import BaseModel, Field
from fastapi import FastAPI, Query, Path, Body

app = FastAPI()


# hello world
@app.get("/")
async def hello():
    return {"msg": "hello mikigo"}


# 路径参数
# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

# 有类型的路径参数
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# 查询参数
@app.get("/items/")
async def read_item(name: str = ""):
    return {"name": name}


# 请求体
class Item(BaseModel):
    name: str
    description: Union[str, None] = None


@app.post("/items/")
async def post_test(item: Item):
    return {"data": item}


# 内建 Query
@app.get("/query/")
async def query_test(
        name: Union[str, None] = Query(default=None, max_length=10)
):
    return {"name": name}


@app.get("/path/{path_id}")
async def path_test(
        path_id: int = Path(default=...),
        name: Union[str, None] = Query(default=..., max_length=10)
):
    results = {"path_id": path_id}
    if name:
        results.update({"name": name})
    return results


@app.post("/body/")
async def body_test(
        item: Item,
        age: int = Body(default=None, gt=0)
):
    results = {"data": item}
    if age:
        results.update({"age": age})
    return {"results": results}

class FieldItem(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="deepin", max_length=300
    )

@app.post("/field/")
async def field_test(
        item: FieldItem,
        age: int = Body(default=None, gt=0)
):
    results = {"data": item}
    if age:
        results.update({"age": age})
    return {"field": results}


if __name__ == '__main__':
    uvicorn.run(
        app="main:app",
        host=os.popen("hostname -I").read().split(" ")[0],
        port=5000,
        reload=True
    )
