from aiogram import Router, F, types
from config import AUDIO_ID_DAY_7
from tgbot.keyboars.user_replay_keyboards import (
    day7_start_keyboard,
    day7_task_keyboard,
    day7_consult_keyboard
)

router = Router()


@router.message(F.text == "/day7")
async def start_day7(message: types.Message):

    with open("files/7/1.txt", encoding="utf-8") as f:
        text = f.read()

    await message.answer(
        text,
        reply_markup=day7_start_keyboard()
    )


@router.callback_query(F.data == "day7_podcast")
async def day7_podcast(callback: types.CallbackQuery):

    await callback.message.answer_audio(
        AUDIO_ID_DAY_7,
        reply_markup=day7_task_keyboard()
    )

    await callback.answer()


@router.callback_query(F.data == "day7_task")
async def day7_task(callback: types.CallbackQuery):

    with open("files/7/task.txt", encoding="utf-8") as f:
        text = f.read()

    await callback.message.answer(
        text,
        reply_markup=day7_consult_keyboard('https://t.me/koshkina_psex')
    )

    await callback.answer()
