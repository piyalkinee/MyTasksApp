from fastapi import APIRouter

from .services.sqlqueries import create_tabels

routes = APIRouter(prefix="/Initialization", tags=["Initialization"])

@routes.post("/initializate")
async def initializate():

    await create_tabels()

    return True