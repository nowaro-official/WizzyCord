import aiosqlite

class Database:
    def __init__(self, db_path):
        self.db_path = db_path

    async def execute(self, query, params=None):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(query, params or ())
            await db.commit()

    async def fetchone(self, query, params=None):
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute(query, params or ()) as cursor:
                return await cursor.fetchone()

    async def fetchall(self, query, params=None):
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute(query, params or ()) as cursor:
                return await cursor.fetchall()
