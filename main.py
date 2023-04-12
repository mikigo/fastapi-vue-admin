import os
from typing import Union, Any

import uvicorn
from fastapi import FastAPI, Query, Path, Body, Cookie, Response, Header, status, Form
from fastapi import File, UploadFile
from pydantic import BaseModel, Field

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


@app.post("/cookieset")
async def cookie_set(response: Response):
    response.set_cookie(key="cookie1", value="mikigocookie11111")
    return {"cookie_id": "ok"}


@app.get("/cookieget")
async def cookie_get(
        ads_id: Union[str, None] = Cookie(default=None)
):
    return {"ads_id": ads_id}


@app.get("/header")
async def header_test(user_agent: Union[str, None] = Header(default=None)):
    return {"User-Agent": user_agent}


@app.post("/rsp_model", response_model=Item)
async def response_model_test(item: Item) -> Any:
    return item

@app.post("/status", status_code=status.HTTP_201_CREATED)
async def status_code_test(name: str):
    return {"name": name}

@app.post("/login")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}


@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


if __name__ == '__main__':
    uvicorn.run(
        app="main:app",
        host=os.popen("hostname -I").read().split(" ")[0],
        port=5000,
        reload=True
    )
