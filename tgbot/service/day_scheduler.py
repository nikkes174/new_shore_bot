import asyncio
from datetime import datetime, time, timedelta

import pytz
from aiogram import Bot
from sqlalchemy import select

from tgbot.db.db import AsyncSessionLocal
from tgbot.db.models import UserModel
from tgbot.service.sender_content import SenderService


class DayScheduler:

    def __init__(self, bot: Bot, send_time: time):
        self.bot = bot
        self.send_time = send_time

    async def start(self):
        print("🟢 DayScheduler запущен")

        while True:
            print("⏳ Ожидание времени отправки...")
            await self.wait_until_time()

            print("🚀 Время пришло. Начинаем обработку пользователей")
            await self.process_users()

    async def wait_until_time(self):

        moscow_tz = pytz.timezone("Europe/Moscow")

        now = datetime.now(moscow_tz)
        target = datetime.combine(now.date(), self.send_time)
        target = moscow_tz.localize(target)

        if now >= target:
            target += timedelta(days=1)

        sleep_seconds = (target - now).total_seconds()

        print(f"🕒 Сейчас (МСК): {now}")
        print(f"🎯 Следующая отправка (МСК): {target}")
        print(f"😴 Спим {sleep_seconds} секунд")

        await asyncio.sleep(sleep_seconds)

    async def process_users(self):
        print("📦 Загружаем пользователей из БД")

        async with AsyncSessionLocal() as session:
            result = await session.execute(select(UserModel))
            users = result.scalars().all()

            print(f"👥 Найдено пользователей: {len(users)}")

            for user in users:
                print(
                    f"➡️ Проверяем user_id={user.user_id}, "
                    f"day={user.day}, create_date={user.create_date}"
                )

                service = SenderService(self.bot, session)
                await service.check_and_update_day(user)
