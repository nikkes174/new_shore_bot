from aiogram import Router, F, types
from config import AUDIO_ID_DAY_5
from tgbot.keyboars.user_replay_keyboards import (
    day5_start_keyboard,
    day5_listened_keyboard,
    day5_task1_done_keyboard,
    day5_done_keyboard,
)

router = Router()


async def send_day5(bot, user_id: int):

    with open("files/5/1.txt", encoding="utf-8") as f:
        text = f.read()

    await bot.send_message(user_id, text, reply_markup=day5_start_keyboard())


@router.message(F.text == "/day5")
async def start_day5(message: types.Message):
    await send_day5(message.bot, message.from_user.id)

    with open("files/5/1.txt", encoding="utf-8") as f:
        text = f.read()

    await message.answer(text, reply_markup=day5_start_keyboard())


@router.callback_query(F.data == "day5_podcast")
async def day5_podcast(callback: types.CallbackQuery):

    await callback.message.answer_audio(
        AUDIO_ID_DAY_5, reply_markup=day5_listened_keyboard()
    )

    await callback.answer()


@router.callback_query(F.data == "day5_task1")
async def day5_task1(callback: types.CallbackQuery):

    with open("files/5/task.txt", encoding="utf-8") as f:
        text = f.read()

    await callback.message.answer(text, reply_markup=day5_task1_done_keyboard())

    await callback.answer()


@router.callback_query(F.data == "day5_task2")
async def day5_task2(callback: types.CallbackQuery):

    with open("files/5/task2.txt", encoding="utf-8") as f:
        text = f.read()

    await callback.message.answer(text, reply_markup=day5_done_keyboard())

    await callback.answer()


@router.callback_query(F.data == "day5_done")
async def day5_done(callback: types.CallbackQuery):

    await callback.message.answer("Отлично. Ещё один день пройден. До завтра.")

    await callback.answer()
