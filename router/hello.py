from fastapi import APIRouter

hello = APIRouter(prefix="/hello", tags=["Hello"])


@hello.get("/")
async def sayhello():
    return {"msg": "Hello FeelGood! "}
