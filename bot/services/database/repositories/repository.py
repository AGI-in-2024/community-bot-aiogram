from sqlalchemy.ext.asyncio import AsyncSession

from bot.services.database.repositories.base import BaseRepository
from bot.services.database.repositories.user_repository import UserRepository


class Repository(BaseRepository):
    user: UserRepository

    def __init__(self, session: AsyncSession):
        super().__init__(session=session)
        self.user = UserRepository(session=session)
