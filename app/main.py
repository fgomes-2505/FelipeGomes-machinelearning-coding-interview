from fastapi import FastAPI

from app.routers.router import router

app = FastAPI(
    title='Live Coding Interview',
)

app.include_router(router)
