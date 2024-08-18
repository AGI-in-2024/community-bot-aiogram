from typing import Final

from aiogram import Router

from bot.handlers.messages import start, hackathons


router: Final[Router] = Router(name=__name__)
router.include_routers(start.router, hackathons.router)
