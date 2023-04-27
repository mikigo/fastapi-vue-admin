import uvicorn
from fastapi import FastAPI

from router.hello import hello
from router.user import user_router
from setting.config import config

app = FastAPI(
    debug=config.DEBUG,
    title=config.APP_NAME,
    version=config.VERSION
)

app.include_router(hello)
app.include_router(user_router)

if __name__ == '__main__':
    uvicorn.run(
        app="main:app",
        host=config.IP,
        port=config.PORT,
        reload=config.RELOAD
    )
