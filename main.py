import uvicorn
from fastapi import FastAPI

import settings
from router.hello import hello
from router.user import user_router

app = FastAPI(
    debug=settings.DEBUG,
    title=settings.APP_NAME,
    version=settings.VERSION,
    redoc_url=None,
)

app.include_router(hello, prefix="/hello", tags=["Hello"])
app.include_router(user_router, prefix="/user", tags=["用户"])

if __name__ == '__main__':
    uvicorn.run(
        app="main:app",
        host=settings.IP,
        port=settings.PORT,
        reload=settings.RELOAD
    )
