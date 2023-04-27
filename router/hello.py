from fastapi import APIRouter

hello = APIRouter()


@hello.get("/")
async def sayhello():
    return {"msg": "Hello FeelGood! "}
