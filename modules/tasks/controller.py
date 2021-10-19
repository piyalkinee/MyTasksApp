from fastapi import APIRouter

routes = APIRouter(prefix="/Tasks", tags=["Tasks"])

@routes.get("/getOne")
async def getOne():
    return 1