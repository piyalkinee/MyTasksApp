from app.database.core import database


async def create_tabels():
    await create_table_groups()
    await create_table_tasks()
    


async def create_table_tasks():
    query = """
    CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL,
        name VARCHAR(32),
        description TEXT,
        date DATE,
        groupId INTEGER,

        PRIMARY KEY (id),
        FOREIGN KEY (groupId) REFERENCES groups (id)
    )
    """

    await database.execute(query)


async def create_table_groups():
    query = """
    CREATE TABLE IF NOT EXISTS groups (
        id SERIAL,
        name VARCHAR(32),

        PRIMARY KEY (id)
    )
    """

    await database.execute(query)
