from config import AUDIO_ID_DAY_1, DOCUMENT_ID_1
from tgbot.keyboars.user_replay_keyboards import day1_next_keyboard, day1_podcast_keyboard, day1_listened_keyboard, \
    day1_video_keyboard, day1_done_keyboard

from aiogram import Router, F, types

router = Router()

# @router.message()
# async def debug_all(message: types.Message):
#     if message.audio:
#         print("AUDIO_ID:", message.audio.file_id)
#     if message.video:
#         print("VIDEO_ID:", message.video.file_id)

@router.message(F.text == "/day1")
async def start_day1(message: types.Message):

    with open("files/1/1.txt", encoding="utf-8") as f:
        text = f.read()

    await message.answer(
        text,
        reply_markup=day1_next_keyboard()
    )
@router.callback_query(F.data == "day1_podcast")
async def day1_podcast(callback: types.CallbackQuery):
    await callback.message.answer_audio(
        AUDIO_ID_DAY_1,
        reply_markup=day1_listened_keyboard()
    )

    await callback.answer()

@router.callback_query(F.data == "day1_step2")
async def day1_step2(callback: types.CallbackQuery):

    with open("files/1/2.txt", encoding="utf-8") as f:
        text = f.read()

    await callback.message.answer(
        text,
        reply_markup=day1_podcast_keyboard()
    )

    await callback.answer()

@router.callback_query(F.data == "day1_practice")
async def day1_practice(callback: types.CallbackQuery):

    with open("files/1/practic.txt", encoding="utf-8") as f:
        text = f.read()

    await callback.message.answer(
        text,
        reply_markup=day1_video_keyboard()
    )

    await callback.answer()

@router.callback_query(F.data == "day1_video")
async def day1_video(callback: types.CallbackQuery):

    await callback.message.answer_document(
        DOCUMENT_ID_1,
        reply_markup=day1_done_keyboard()
    )

    await callback.answer()


    await callback.answer()

@router.callback_query(F.data == "day1_done")
async def day1_done(callback: types.CallbackQuery):

    await callback.message.answer(
        "Отлично, первый день пройден. Продолжим завтра."
    )


    await callback.answer()


