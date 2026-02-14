import asyncio
import logging
from datetime import time
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommandScopeDefault, MenuButtonCommands, BotCommand

from tgbot.db.db import init_db
from tgbot.hadlers.user import router as user_router
from tgbot.hadlers.day_1 import router as day_one_router
from tgbot.hadlers.day_4 import router as day_four_router
from tgbot.hadlers.day_2 import router as day_two_router
from tgbot.hadlers.day_3 import router as day_three_router
from config import BOT_TOKEN
from tgbot.service.day_scheduler import DayScheduler
from tgbot.hadlers.day_5 import router as day_five_router
from tgbot.hadlers.day_6 import router as day_six_router
from tgbot.hadlers.day_7 import router as day_seven_router



async def on_startup(bot: Bot):

    commands = [
        BotCommand(command="start", description="Перезапуск бота"),
    ]

    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())

    await bot.set_chat_menu_button(menu_button=MenuButtonCommands())


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.message.middleware(lambda handler, event, data: handler(event, data))

    await init_db()
    dp.include_router(user_router)
    dp.include_router(day_one_router)
    dp.include_router(day_two_router)
    dp.include_router(day_three_router)
    dp.include_router(day_four_router)
    dp.include_router(day_five_router)
    dp.include_router(day_six_router)
    dp.include_router(day_seven_router)

    await on_startup(bot)

    scheduler = DayScheduler(bot, send_time=time(hour=15, minute=40))

    asyncio.create_task(scheduler.start())

    me = await bot.get_me()
    logging.info(f"🤖 Бот запущен: @{me.username} ({me.id})")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
