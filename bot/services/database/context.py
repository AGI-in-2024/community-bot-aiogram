import asyncio

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from bot.services.database.repositories.repository import Repository


class DBContext:
    __slots__ = ("session_pool", "session")

    def __init__(self, session_pool: async_sessionmaker[AsyncSession]):
        self.session_pool = session_pool
        self.session = None

    async def __aenter__(self):
        self.session = await self.session_pool().__aenter__()
        return Repository(session=self.session)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session is None:
            return
        task: asyncio.Task = asyncio.create_task(self.session.close())
        await asyncio.shield(task)
        self.session = None
