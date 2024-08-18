from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from typing_extensions import Final
from structlog import get_logger

router: Final[Router] = Router(name=__name__)
logger = get_logger()


@router.message(CommandStart())
async def start_command(
        message: Message
):
    await logger.adebug(
        "Start user %s - %i",
        message.from_user.username,
        message.from_user.id
    )

    await message.answer(
        "Привет. Я пока не отвечаю."
    )
