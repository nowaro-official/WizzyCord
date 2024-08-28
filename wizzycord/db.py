from typing import Any, Optional, List, Tuple
import aiosqlite

class Database:
    def __init__(self, db_path: str):
        self.db_path = db_path

    async def execute(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> None:
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(query, params or ())
            await db.commit()

    async def fetchone(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> Optional[Tuple[Any, ...]]:
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute(query, params or ()) as cursor:
                return await cursor.fetchone()

    async def fetchall(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> List[Tuple[Any, ...]]:
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute(query, params or ()) as cursor:
                return await cursor.fetchall()

    async def executemany(self, query: str, param_list: List[Tuple[Any, ...]]) -> None:
        async with aiosqlite.connect(self.db_path) as db:
            await db.executemany(query, param_list)
            await db.commit()
