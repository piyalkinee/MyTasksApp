from fastapi import APIRouter

routes = APIRouter(prefix="/Initialization", tags=["Initialization"])

@routes.get("/getOne")
async def getOne():
    return 1