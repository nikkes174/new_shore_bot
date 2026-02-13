
from tgbot.keyboars.user_replay_keyboards import start_keyboard, hesitate_keyboard, pay_only_keyboard, tips_keyboard, \
    pay_or_start_keyboard, day1_next_keyboard, payment_confirm_keyboard

from aiogram import Router, F, types

router = Router()



# @router.message()
# async def debug_all(message: types.Message):
#     if message.video:
#         print("VIDEO_ID:", message.video.file_id)
#
#     if message.document:
#         print("DOCUMENT_ID:", message.document.file_id)
#
#     if message.video_note:
#         print("VIDEO_NOTE_ID:", message.video_note.file_id)
#
#     if message.audio:
#         print("AUDIO_ID:", message.audio.file_id)


@router.message(F.text == "/start")
async def start(message: types.Message):

    first_text = (
        "Привет.\n\n"
        "Я знаю, что сейчас ты чувствуешь себя так, будто по тебе проехали катком. "
        "Мало воздуха, всё вокруг потеряло цвет, а в голове — один нескончаемый диалог с ним. "
        "Ты ловишь себя на том, что снова и снова прокручиваешь «а что, если», "
        "представляешь сцены из прошлого или выдуманного будущего. "
        "Это выматывает, опустошает и не дает сделать шаг вперед.\n\n"
        "Я не стану рассказывать тебе о тревожном типе привязанности или искать причины в прошлом. "
        "Сейчас важно, чтобы ты обрела опору.\n\n"
        "Когда человек тонет, ему не нужен тот, кто будет учить его плавать. "
        "Ему нужен тот, кто поможет выбраться из воды. "
        "Именно этим мы с тобой и займемся.\n\n"
        "Я, Лидия Кошкина, — твой психолог и проводник на эти 7 дней. "
        "Мы будем делать конкретные шаги, чтобы ты смогла выйти на свой новый берег."
    )

    await message.answer(first_text)

    await message.answer_video_note(
        "DQACAgIAAxkBAAMIaYzFBSObN5j5ay1wrEUSulYzD8QAAlSMAAJeomBIqSFPR3i258U6BA"
    )

    await message.answer_video_note(
        "DQACAgIAAxkBAAMJaYzFBb1eDBnU8TaI5PLU5RYVhHgAAl-MAAJeomBIcANV_IHxB2g6BA"
    )

    second_text = (
        "Что тебя ждет в этом путешествии на 7 дней:\n\n"
        "• Ежедневный мини-подкаст (голосовое): поддержка, объяснения и психологические техники. "
        "Ты сможешь слушать, когда удобно — за чаем, в дороге, перед сном.\n\n"
        "• Текстовые разборы: простые и ясные объяснения того, что происходит с твоими эмоциями, мыслями и телом.\n\n"
        "• Конкретные задания-упражнения: четкие действия на 10–15 минут в день, "
        "которые реально меняют фокус внимания и состояние.\n\n"
        "• Безопасное пространство: здесь только ты и твои чувства. "
        "Никаких советов «возьми себя в руки» или «заведи нового». "
        "Только бережная работа с болью.\n\n"
        "Результат, к которому мы идем:\n"
        "Свобода от навязчивых мыслей. Спокойствие вместо паники. "
        "И вера в то, что счастье возможно — и оно ждет тебя в будущем, "
        "где ты — главная героиня.\n\n"
        "Готова сделать первый шаг к своему новому берегу?"
    )

    await message.answer(
        second_text,
        reply_markup=start_keyboard()
    )



@router.callback_query(F.data == "hesitate")
async def hesitate_handler(callback: types.CallbackQuery):
    text = (
        "Ты не готова оплатить сразу 7 дней. Я понимаю тебя.\n\n"
        "Уверена, что ты уже много всего перепробовала. "
        "Что-то не помогло, что-то помогло, но не надолго.\n\n"
        "Но ты уже пришла сюда, и позволь просто дать тебе несколько советов, "
        "как облегчить свою боль:\n\n"
        "1. Не замыкайся в себе. Неужели весь твой огромный мир свернулся "
        "калачиком у ног этого мужчины? Ты вложила столько сил и эмоций "
        "в эти отношения — значит, они у тебя были. Ты пришла с этим к нему. "
        "Не он тебе это дал и не ему это забирать.\n\n"
        "2. Не старайся «заглушить» одиночество срочными знакомствами. "
        "Сейчас ты уязвима для опытных манипуляторов или абьюзеров в маске «спасителя», которые легко разглядят отчаяние.\n"
        "Даже встретив достойного мужчину, ты будешь в тревоге от любого сообщения вроде: «Привет. Как дела?». "
        "Пока нет внутренней опоры, невозможно построить здоровые отношения, , даже с самым хорошим человеком."
    )

    await callback.message.answer(
        text,
        reply_markup=hesitate_keyboard()
    )

    await callback.answer()

@router.callback_query(F.data == "more_tips")
async def more_tips_handler(callback: types.CallbackQuery):
    text = (
        "Спасибо, что доверяешь мне.\n\n"
        "Не все советы тебе могут понравиться. Так работает сопротивление. "
        "Это защитный механизм психики. Мозг очень ленивый и хочет, чтобы ты шла "
        "только привычным путём.\n\n"
        "Не иди на поводу у этих уловок. Тебе нужны новые нейронные связи, "
        "новые пути, новые решения.\n\n"
        "Советы:\n\n"
        "1. Пожалуйста, не прибегай к алкоголю. Это худший советчик. "
        "Он даст облегчение на пару часов, а затем — токсичный стыд.\n\n"
        "2. Не ходи к гадалкам и волшебницам. "
        "Нет силы, которая построит твоё счастье за тебя. "
        "Только твои действия ведут к результату."
    )

    await callback.message.answer(
        text,
        reply_markup=tips_keyboard()
    )

    await callback.answer()

@router.callback_query(F.data == "final_push")
async def final_push_handler(callback: types.CallbackQuery):
    text = (
        "Я надеюсь, ты не просто читаешь мои советы, а действительно им следуешь.\n\n"
        "Знания без действий не дадут тебе свободу.\n\n"
        "Когда я прошла путь освобождения от постоянных мыслей о НЁМ, "
        "я даже отказалась от курения. Это было как прозрение:\n\n"
        "«Какого черта?! Это как верёвка на моей шее — поводок, "
        "за который дергает меня зависимость. Ненавижу!»\n\n"
        "Неважно, никотиновая зависимость или любовная — "
        "я родилась свободной от навязчивых мыслей.\n\n"
        "Твой выбор сейчас:\n\n"
        "✅ Продолжать терпеть боль, заливая её сериалами и едой.\n\n"
        "✅ Ждать записи к специалисту и платить от 3 000 ₽ за сессию.\n\n"
        "✅ ДАТЬ СЕБЕ ПРОСТОЙ И БЕЗОПАСНЫЙ ШАНС. "
        "Потратить 15 минут в день на себя, чтобы через месяц "
        "почувствовать облегчение и интерес к новому дню."
    )

    await callback.message.answer(
        text,
        reply_markup=pay_or_start_keyboard()

    )

    await callback.answer()

from datetime import date
from sqlalchemy import select
from tgbot.db.db import AsyncSessionLocal
from tgbot.db.models import UserModel
from tgbot.keyboars.user_replay_keyboards import day1_next_keyboard

@router.callback_query(F.data == "start_day1_direct")
async def start_day1_direct(callback: types.CallbackQuery):

    async with AsyncSessionLocal() as session:

        result = await session.execute(
            select(UserModel).where(
                UserModel.user_id == callback.from_user.id
            )
        )
        user = result.scalar_one_or_none()

        # Если пользователя нет — создаём
        if not user:
            user = UserModel(
                user_id=callback.from_user.id,
                user_name=callback.from_user.username,
                create_date=date.today(),
                day=1
            )
            session.add(user)
            await session.commit()

        # Если есть — просто сбрасываем на 1 день
        else:
            user.day = 1
            user.create_date = date.today()
            await session.commit()

    # Отправляем первый день
    with open("files/1/1.txt", encoding="utf-8") as f:
        text = f.read()

    await callback.message.answer(
        text,
        reply_markup=day1_next_keyboard()
    )

    await callback.answer()

@router.callback_query(F.data == "pay")
async def pay_handler(callback: types.CallbackQuery):
    text = (
        "Перед покупкой не забудь ознакомиться с "
        "<a href='https://telegra.ph/Publichnaya-oferta-o-zaklyuchenii-dogovora-ob-okazanii-informacionnyh-uslug-02-13'>договором оферты</a> "
        "и "
        "<a href='https://telegra.ph/POLITIKA-v-otnoshenii-obrabotki-personalnyh-dannyh-02-13-17'>политикой обработки персональных данных</a>."
    )

    await callback.message.answer(
        text,
        parse_mode="HTML",
        disable_web_page_preview=True ,

        reply_markup=payment_confirm_keyboard()
    )

    await callback.answer()
