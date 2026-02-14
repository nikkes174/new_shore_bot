from tgbot.keyboars.user_replay_keyboards import (
    day3_podcast_keyboard,
    day3_task_keyboard,
    day3_done_keyboard,
)

from config import AUDIO_ID_DAY_3

from aiogram import Router, F, types

router = Router()


async def send_day3(bot, user_id: int):
    with open("files/3/1.txt", encoding="utf-8") as f:
        text = f.read()

    await bot.send_message(
        user_id,
        text,
        reply_markup=day3_podcast_keyboard()
    )


@router.message(F.text == "/day3")
async def start_day3(message: types.Message):
    await send_day3(message.bot, message.from_user.id)



@router.message(F.text == "/day3")
async def start_day3(message: types.Message):
    await send_day3(message.bot, message.from_user.id)

    text = (
        "ДЕНЬ 3. Эмоции.\n\n"
        "Предыдущие два дня мы говорили о том, что происходит с телом, "
        "а точнее о его реакциях. Реакции тела и реакции поведения следуют "
        "за определенными эмоциями.\n\n"
        "Т.е. вначале эмоция, затем – реакция.\n\n"
        "Когда мы чувствуем радость, тело реагирует возбуждением. "
        "Когда испытываем счастье — чувствуем расслабление и тепло. "
        "На отрицательные эмоции тело реагирует напряжением, болью.\n\n"
        "То, что происходит с твоим телом, мы уже разобрали. "
        "Пришло время разобраться в том, какие на самом деле эмоции "
        "запускают эти реакции. Можно ли их изменить?\n\n"
        "Продолжение в подкасте."
    )

    await message.answer(text, reply_markup=day3_podcast_keyboard())


@router.callback_query(F.data == "day3_podcast")
async def day3_podcast(callback: types.CallbackQuery):

    await callback.message.answer_audio(
        AUDIO_ID_DAY_3, reply_markup=day3_task_keyboard()
    )

    await callback.answer()


@router.callback_query(F.data == "day3_task")
async def day3_task(callback: types.CallbackQuery):

    with open("files/3/2.txt", encoding="utf-8") as f:
        text = f.read()

    await callback.message.answer(
        text,
        reply_markup=day3_done_keyboard()
    )

    await callback.answer()



@router.callback_query(F.data == "day3_done")
async def day3_done(callback: types.CallbackQuery):
    text = (
        "Отлично. Послушай сегодня приятную музыку, прими ванну "
        "и не забудь проветрить комнату перед сном.\n\n"
        "Завтра поговорим о том, как избавиться от навязчивых мыслях "
        "о сексе с ним. Нам понадобится пластилин.\n\n"
        "До завтра."
    )

    await callback.message.answer(text)
    await callback.answer()
