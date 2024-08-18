from aiogram import Dispatcher

from bot.handlers import messages


def setup_routers(dispatcher: Dispatcher):
    dispatcher.include_routers(
        messages.router
    )


__all__ = "setup_routers"
