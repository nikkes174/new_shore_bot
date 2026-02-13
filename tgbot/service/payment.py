import asyncio
import os
from datetime import date
from dotenv import load_dotenv
from yookassa import Configuration, Payment

from tgbot.db.crud_users import UserCrud
from tgbot.db.db import AsyncSessionLocal
from tgbot.service.sender_content import SenderService

load_dotenv()


class PaymentUtils:

    def __init__(self):
        self.yookassa_id = os.getenv("YOOKASSA_SHOP_ID")
        self.yookassa_key = os.getenv("YOOKASSA_SECRET_KEY")

        Configuration.account_id = self.yookassa_id
        Configuration.secret_key = self.yookassa_key

        self.active_payment_users = set()
        self._amount = 1

    def check_payment_status(self, payment_id: str):
        try:
            payment = Payment.find_one(payment_id)
            return payment.status, payment.metadata
        except Exception:
            return None, None

    async def create_payment_async(self, payload: dict):
        return await asyncio.to_thread(Payment.create, payload)

    async def create_payment(
            self,

            user_id: int,

    ):
        return_url = "https://t.me/BlackGateGuard_bot"

        payload = {
            "amount": {"value": f"{self._amount:.2f}", "currency": "RUB"},
            "confirmation": {"type": "redirect", "return_url": return_url},
            "capture": True,
            "description": f"Подписка user={user_id}",
            "metadata": {
                "user_id": str(user_id),
            },
        }

        payment = await self.create_payment_async(payload)
        return payment.id, payment.confirmation.confirmation_url

    async def poll_payment(self, payment_id):
        for i in range(10):
            status, metadata = await asyncio.to_thread(
                self.check_payment_status, payment_id
            )

            if status == "succeeded":
                return True, metadata

            await asyncio.sleep(min(10 * (i + 1), 60))

        return False, None

    async def check_payment_loop(
            self,
            payment_id: str,
            user_id: int,
            username: str,
            bot,
    ):
        if user_id in self.active_payment_users:
            return

        self.active_payment_users.add(user_id)

        async with AsyncSessionLocal() as session:
            user_crud = UserCrud(session)

            try:
                ok, metadata = await self.poll_payment(payment_id)
                if not ok:
                    return

                user = await user_crud.get_user(user_id)

                if not user:
                    user = await user_crud.add_user(
                        user_id=user_id,
                        user_name=username,
                        create_date=date.today(),
                        day=1,
                    )

                await bot.send_message(
                    user_id,
                    "🎉 Оплата прошла успешно! Материал первого дня уже доступен."
                )

                day_service = SenderService(bot, session)
                await day_service.send_day_content(user)

            except Exception as e:
                print("[PAYMENT LOOP ERROR]:", e)
                try:
                    await bot.send_message(
                        user_id,
                        "❌ Ошибка при обработке оплаты."
                    )
                except:
                    pass
            finally:
                self.active_payment_users.remove(user_id)
