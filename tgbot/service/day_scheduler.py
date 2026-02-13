import asyncio
from datetime import datetime, date, time, timedelta

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
        while True:
            await self.wait_until_time()
            await self.process_users()

    async def wait_until_time(self):
        now = datetime.now()
        target = datetime.combine(now.date(), self.send_time)

        if now >= target:
            target += timedelta(days=1)

        sleep_seconds = (target - now).total_seconds()
        await asyncio.sleep(sleep_seconds)

    async def process_users(self):
        async with AsyncSessionLocal() as session:
            result = await session.execute(select(UserModel))
            users = result.scalars().all()

            for user in users:
                service = SenderService(self.bot, session)
                await service.check_and_update_day(user)
