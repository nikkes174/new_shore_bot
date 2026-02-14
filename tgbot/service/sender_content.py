import pytz
from datetime import datetime

from aiogram import Bot
from sqlalchemy.ext.asyncio import AsyncSession

from tgbot.db.models import UserModel
from tgbot.hadlers.day_1 import send_day1
from tgbot.hadlers.day_2 import send_day2
from tgbot.hadlers.day_3 import send_day3
from tgbot.hadlers.day_4 import send_day4
from tgbot.hadlers.day_5 import send_day5
from tgbot.hadlers.day_6 import send_day6
from tgbot.hadlers.day_7 import send_day7


class SenderService:

    def __init__(self, bot: Bot, session: AsyncSession):
        self.bot = bot
        self.session = session

    async def check_and_update_day(self, user: UserModel):
        if not user.create_date:
            print(f"⚠️ У user_id={user.user_id} нет create_date")
            return

        moscow_tz = pytz.timezone("Europe/Moscow")
        today = datetime.now(moscow_tz).date()

        passed_days = user.day + 1

        print(
            f"📊 user_id={user.user_id} | "
            f"create_date={user.create_date} | "
            f"today={today} | "
            f"passed_days={passed_days} | "
            f"current_day={user.day}"
        )

        if passed_days > 7:
            print("🛑 Курс завершён")
            return

        if passed_days > user.day:
            print(f"✅ Обновляем день до {passed_days}")

            user.day = passed_days
            await self.session.commit()

            await self.send_day_content(user)
        else:
            print("⏭ Обновление не требуется")

    async def send_day_content(self, user: UserModel):

        if user.day == 1:
            await send_day1(self.bot, user.user_id)

        elif user.day == 2:
            await send_day2(self.bot, user.user_id)

        elif user.day == 3:
            await send_day3(self.bot, user.user_id)

        elif user.day == 4:
            await send_day4(self.bot, user.user_id)

        elif user.day == 5:
            await send_day5(self.bot, user.user_id)

        elif user.day == 6:
            await send_day6(self.bot, user.user_id)

        elif user.day == 7:
            await send_day7(self.bot, user.user_id)
