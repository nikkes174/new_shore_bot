from aiogram import Router, F, types
from config import AUDIO_ID_DAY_4, DOCUMENT_ID_2
from tgbot.keyboars.user_replay_keyboards import (
    day4_start_keyboard,
    day4_video_keyboard,
    day4_done_keyboard
)

router = Router()


@router.message(F.text == "/day4")
async def start_day4(message: types.Message):

    with open("files/4/1.txt", encoding="utf-8") as f:
        text = f.read()

    await message.answer(
        text,
        reply_markup=day4_start_keyboard()
    )


@router.callback_query(F.data == "day4_podcast")
async def day4_podcast(callback: types.CallbackQuery):

    await callback.message.answer_audio(
        AUDIO_ID_DAY_4
    )

    await callback.answer()


@router.callback_query(F.data == "day4_practice")
async def day4_practice(callback: types.CallbackQuery):

    text = (
        "Сегодня мы сделаем технику «Диафрагма» из нейролингвистического "
        "программирования, которая поможет тебе уйти от идеализации "
        "и избавит тебя от сексуальных флешбеков с бывшим партнёром.\n\n"
        "Прежде чем включить видео, подготовься.\n\n"
        "Возьми пластилин и вылепи из него макет члена твоего бывшего, "
        "лучше в натуральную величину.\n\n"
        "Возможно, сейчас тебе это кажется странным. Доверься. "
        "Техника очень действенная."
    )

    await callback.message.answer(
        text,
        reply_markup=day4_video_keyboard()
    )

    await callback.answer()


@router.callback_query(F.data == "day4_video")
async def day4_video(callback: types.CallbackQuery):

    await callback.message.answer_document(
        DOCUMENT_ID_2,
        reply_markup=day4_done_keyboard()
    )

    await callback.answer()


@router.callback_query(F.data == "day4_done")
async def day4_done(callback: types.CallbackQuery):

    text = (
        "Отлично.\n\n"
        "Постарайся на остаток дня исключить сладкое.\n"
        "Замени его любыми физическими упражнениями."
    )

    await callback.message.answer(text)

    await callback.answer()
