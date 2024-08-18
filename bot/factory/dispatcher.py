from aiogram import Dispatcher
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker

from bot.handlers import setup_routers
from bot.lib.settings import Settings
from bot.middlewares.outer.database import DBSessionMiddleware
from bot.middlewares.outer.user import UserMiddleware


async def _setup_outer_middlewares(dispatcher: Dispatcher, settings: Settings) -> None:
    engine: AsyncEngine = create_async_engine(url=settings.postgres.dsn)
    pool = dispatcher["session_pool"] = async_sessionmaker(engine, expire_on_commit=False)
    dispatcher.update.outer_middleware(DBSessionMiddleware(session_pool=pool))
    dispatcher.update.outer_middleware(UserMiddleware())


def _setup_inner_middlewares(dispatcher: Dispatcher) -> None:
    dispatcher.callback_query.middleware(CallbackAnswerMiddleware())


async def create_dispatcher(settings: Settings) -> Dispatcher:
    dispatcher: Dispatcher = Dispatcher(
        name="main"
    )
    setup_routers(dispatcher)
    await _setup_outer_middlewares(dispatcher, settings)
    _setup_inner_middlewares(dispatcher)

    return dispatcher
