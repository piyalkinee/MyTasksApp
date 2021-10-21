import datetime

from app.database.core import database


async def insert_group(group_name: str):
    query = f"INSERT INTO groups (name) VALUES ('{group_name}') RETURNING id;"

    return await database.fetch_one(query)


async def insert_task(task_name: str, task_description: str, group_owner_id: str):
    current_time = datetime.date.today()
    print(current_time)
    query = f"INSERT INTO tasks (name,description,date,groupId) VALUES ('{task_name}','{task_description}','{current_time}',{group_owner_id}) RETURNING id;"

    return await database.fetch_one(query)


async def select_task_from_group(group_id: int):
    query = f"SELECT * FROM tasks WHERE groupId = {group_id}"

    return [t for t in await database.fetch_all(query)]
