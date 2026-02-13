from aiogram import Router, F, types
from config import AUDIO_ID_DAY_6
from tgbot.keyboars.user_replay_keyboards import (
    day6_start_keyboard,
    day6_listened_keyboard,
    day6_done_keyboard
)

router = Router()


@router.message(F.text == "/day6")
async def start_day6(message: types.Message):

    with open("files/6/1.txt", encoding="utf-8") as f:
        text = f.read()

    await message.answer(
        text,
        reply_markup=day6_start_keyboard()
    )


@router.callback_query(F.data == "day6_podcast")
async def day6_podcast(callback: types.CallbackQuery):

    await callback.message.answer_audio(
        AUDIO_ID_DAY_6,
        reply_markup=day6_listened_keyboard()
    )

    await callback.answer()


@router.callback_query(F.data == "day6_task")
async def day6_task(callback: types.CallbackQuery):

    with open("files/6/task.txt", encoding="utf-8") as f:
        text = f.read()

    await callback.message.answer(
        text,
        reply_markup=day6_done_keyboard()
    )

    await callback.answer()


@router.callback_query(F.data == "day6_done")
async def day6_done(callback: types.CallbackQuery):

    await callback.message.answer(
        "Отлично. Впереди заключительный день.\nДо завтра."
    )

    await callback.answer()
