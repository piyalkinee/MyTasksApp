from fastapi import FastAPI
from app.database.core import database
from .routes import routes

app = FastAPI(title="School")

app.include_router(routes)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()