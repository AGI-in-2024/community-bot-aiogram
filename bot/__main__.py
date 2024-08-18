from structlog import get_logger

from bot.factory.bot import create_bot
from bot.factory.dispatcher import create_dispatcher
from bot.lib.settings import get_settings

logger = get_logger()


async def main():
    settings = get_settings()

    bot = create_bot(settings)
    dispatcher = await create_dispatcher(settings)
    await bot.delete_webhook(drop_pending_updates=True)

    await logger.ainfo(
        "Community bot - start."
    )

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    import uvloop

    uvloop.run(main())
