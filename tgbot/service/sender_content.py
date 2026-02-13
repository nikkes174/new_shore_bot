
from datetime import date
from aiogram import Bot, types
from sqlalchemy.ext.asyncio import AsyncSession

from tgbot.db.models import UserModel


class SenderService:

    def __init__(self, bot: Bot, session: AsyncSession):
        self.bot = bot
        self.session = session

    async def check_and_update_day(self, user: UserModel):
        if not user.create_date:
            return

        today = date.today()
        passed_days = (today - user.create_date).days + 1
        if passed_days > 7:
            return

        if passed_days > user.day:
            user.day = passed_days
            await self.session.commit()

            await self.send_day_content(user)

