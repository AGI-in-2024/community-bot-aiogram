from sqlmodel import select

from bot.services.database.models.user import User
from bot.services.database.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    async def create(self, user: User) -> User:
        self.session.add(user)
        await self.session.commit()
        return user

    async def get(self, user_id: int) -> User:
        return (
            await self.session.execute(
                select(User).where(User.id == user_id)
            )
        ).scalar_one_or_none()
