from aiogram import Router, F, types
from config import AUDIO_ID_DAY_2, DOCUMENT_ID_2
from tgbot.keyboars.user_replay_keyboards import (
    day2_step2_keyboard,
    day2_podcast_keyboard,
    day2_listened_keyboard,
    day2_done_keyboard, day2_written_keyboard,
)

router = Router()


async def send_day2(bot, user_id: int):

    with open("files/2/1.txt", encoding="utf-8") as f:
        text1 = f.read()

    await bot.send_message(user_id, text1)

    with open("files/2/2.txt", encoding="utf-8") as f:
        text2 = f.read()

    await bot.send_message(user_id, text2, reply_markup=day2_step2_keyboard())


@router.message(F.text == "/day2")
async def start_day2(message: types.Message):
    await send_day2(message.bot, message.from_user.id)


    with open("files/2/1.txt", encoding="utf-8") as f:
        text1 = f.read()

    await message.answer(text1)

    with open("files/2/2.txt", encoding="utf-8") as f:
        text2 = f.read()

    await message.answer(text2, reply_markup=day2_step2_keyboard())


@router.callback_query(F.data == "day2_step2")
async def day2_step2(callback: types.CallbackQuery):

    text = (
        "Отлично. Эти шаги - база, которая делает тягу тише и короче. "
        "Я знаю, что, возможно, эти шаги кажутся тебе сложными. "
        "У тебя так мало сил. Но подумай, сколько сил ты тратишь "
        "на ожидание сообщения от него, на воспоминания и придумывание "
        "бесконечных диалогов с ним. Взамен получаешь только тоску.\n\n"
        "Слушай мой подкаст, это добавит тебе решительности."
    )

    await callback.message.answer(text, reply_markup=day2_podcast_keyboard())

    await callback.answer()

@router.callback_query(F.data == "day2_task")
async def day2_task(callback: types.CallbackQuery):

    text = (
        "Задание:\n"
        "Составь список триггеров, которые могут привести тебя к срыву. "
        "Составь план, как ты будешь справляться. "
        "Включи в этот план данную технику и используй шаги и способы, "
        "которые ты сегодня выучила."
    )

    await callback.message.answer(
        text,
        reply_markup=day2_written_keyboard()
    )

    await callback.answer()

@router.callback_query(F.data == "day2_written")
async def day2_written(callback: types.CallbackQuery):

    await callback.message.answer(
        '<b>Техника "Растворение тяги"</b>',
        parse_mode="HTML"
    )

    await callback.message.answer_document(
        DOCUMENT_ID_2,
        reply_markup=day2_done_keyboard()
    )

    await callback.answer()

@router.callback_query(F.data == "day2_podcast")
async def day2_podcast(callback: types.CallbackQuery):

    await callback.message.answer_audio(
        AUDIO_ID_DAY_2, reply_markup=day2_listened_keyboard()
    )

    await callback.answer()




@router.callback_query(F.data == "day2_done")
async def day2_done(callback: types.CallbackQuery):

    text = (
        "Отлично. Ты увидела цвет, который тебе помогает. "
        "Это твой новый якорь. Постарайся окружить себя предметами этого цвета - "
        "одежда, чехол для телефона, предметы обстановки или просто лист бумаги "
        "этого цвета. Смотри на него, когда будешь чувствовать тягу.\n\n"
        "Сегодня был сложный день, но ты справилась. Ты супер! До завтра."
    )

    await callback.message.answer(text)
    await callback.answer()
