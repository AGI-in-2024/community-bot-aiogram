from typing import Callable, Dict, Any, Awaitable, cast

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Chat

from bot.services.database.models import User
from bot.services.database.repositories.repository import Repository


class UserMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        aiogram_user: User | None = data.get("event_from_user")
        chat: Chat | None = data.get("event_chat")
        if aiogram_user is None or chat is None or aiogram_user.is_bot:
            return await handler(event, data)

        repository: Repository = data["repository"]
        user: User | None = await repository.user.get(user_id=aiogram_user.id)

        if user is None:
            user = User.from_aiogram_user(
                user=aiogram_user
            )
            await repository.user.create(user)

        data["user"] = user
        return await handler(event, data)
