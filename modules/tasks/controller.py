from fastapi import APIRouter

from .services.sqlqueries import insert_group, insert_task, select_task_from_group

routes = APIRouter(prefix="/Tasks", tags=["Tasks"])


@routes.post("/AddGroup")
async def add_group(group_name: str):
    return await insert_group(group_name)


@routes.post("/AddTask")
async def add_task(task_name: str, task_description: str, group_owner_id: str):
    return await insert_task(task_name, task_description, group_owner_id)


@routes.get("/GetTaskFromGroup")
async def get_tasks_from_group(group_id: int):
    return await select_task_from_group(group_id)
