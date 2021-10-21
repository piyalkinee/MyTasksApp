import databases

DATABASE_NAME = "mytasks"
DATABASE_URL = f"postgres://postgres:1231@postgres/{DATABASE_NAME}"

database = databases.Database(DATABASE_URL)
