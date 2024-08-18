from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode

from bot.lib.settings import Settings
from bot.utils.serializable import *


def create_bot(settings: Settings) -> Bot:
    session: AiohttpSession = AiohttpSession(
        json_dumps=encode,
        json_loads=decode
    )

    return Bot(
        token=settings.bot.token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        ),
        session=session
    )
