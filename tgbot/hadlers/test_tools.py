from aiogram import Router, F, types
from sqlalchemy import select
from tgbot.db.db import AsyncSessionLocal
from tgbot.db.models import UserModel
from tgbot.service.sender_content import SenderService

router = Router()


@router.callback_query(F.data == "test_next_day")
async def test_next_day(callback: types.CallbackQuery):

    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(UserModel).where(UserModel.user_id == callback.from_user.id)
        )
        user = result.scalar_one_or_none()

        if not user:
            await callback.answer("Пользователь не найден", show_alert=True)
            return

        user.day += 1
        await session.commit()

        service = SenderService(callback.bot, session)
        await service.send_day_content(user)

    await callback.answer()
