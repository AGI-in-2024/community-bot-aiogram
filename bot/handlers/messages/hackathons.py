from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from typing_extensions import Final
from structlog import get_logger

from bot.services.database.models.user import User
from bot.services.database.repositories.repository import Repository

router: Final[Router] = Router(name=__name__)
logger = get_logger()


@router.message(Command("hackathons"))
async def hackathons_handler(
        message: Message,
        user: User,
        repository: Repository
):
    await message.answer(
        user.description if user.description else "У вас нет описания."
    )
