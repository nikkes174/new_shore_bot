# 🤖 AI Code Bundle

## 📌 Параметры
- **Files:** `[]`
- **Dirs:** `['.']`
- **Extensions:** `['.css', '.html', '.js', '.json', '.py']`

---


# 📂 Директория: `C:\Users\pride\Desktop\python\LydaBot`

## 📁 `.`

## 📄 `bot.py`

```python
import asyncio
import logging
from datetime import time
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommandScopeDefault, MenuButtonCommands, BotCommand

from tgbot.db.db import init_db
from tgbot.hadlers.user import router as user_router
from tgbot.hadlers.day_1 import router as day_one_router
from tgbot.hadlers.day_4 import router as day_four_router
from tgbot.hadlers.day_2 import router as day_two_router
from tgbot.hadlers.day_3 import router as day_three_router
from config import BOT_TOKEN
from tgbot.service.day_scheduler import DayScheduler
from tgbot.hadlers.day_5 import router as day_five_router
from tgbot.hadlers.day_6 import router as day_six_router
from tgbot.hadlers.day_7 import router as day_seven_router
from datetime import datetime, timedelta
from tgbot.hadlers.test_tools import router as test_router


async def on_startup(bot: Bot):

    commands = [
        BotCommand(command="start", description="Перезапуск бота"),

    ]


    await bot.set_my_commands(
        commands,
        scope=BotCommandScopeDefault()
    )


    await bot.set_chat_menu_button(
        menu_button=MenuButtonCommands()
    )




async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.message.middleware(lambda handler, event, data: handler(event, data))

    await init_db()
    dp.include_router(user_router)
    dp.include_router(day_one_router)
    dp.include_router(day_two_router)
    dp.include_router(day_three_router)
    dp.include_router(day_four_router)
    dp.include_router(day_five_router)
    dp.include_router(day_six_router)
    dp.include_router(day_seven_router)
    dp.include_router(test_router)

    await on_startup(bot)

    scheduler = DayScheduler(bot, send_time=time(hour=10, minute=0))

    asyncio.create_task(scheduler.start())

    me = await bot.get_me()
    logging.info(f"🤖 Бот запущен: @{me.username} ({me.id})")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

```

## 📄 `config.py`

```python
import os

from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv("DB")

YOOKASSA_SHOP_ID = os.getenv('YOOKASSA_SHOP_ID')

YOOKASSA_SECRET_KEY=os.getenv('YOOKASSA_SECRET_KEY')

YOOKASSA_RETURN_URL =''

BOT_TOKEN = os.getenv('BOT_TOKEN')

INTRO_VIDEO_1 = "DQACAgIAAxkBAAMIaYzFBSObN5j5ay1wrEUSulYzD8QAAlSMAAJeomBIqSFPR3i258U6BA"
INTRO_VIDEO_2 = "DQACAgIAAxkBAAMJaYzFBb1eDBnU8TaI5PLU5RYVhHgAAl-MAAJeomBIcANV_IHxB2g6BA"
AUDIO_ID_DAY_1 = 'CQACAgIAAxkBAAM2aYzLr9RjY-MolJvOUpc4LWFXtNQAAqOVAAK2eWFIWVYbBu1uUUo6BA'
AUDIO_ID_DAY_2 = 'CQACAgIAAxkBAAM4aYzORZStami5reL1Mwv_vaExOjEAAgiWAAK2eWFI4nvvYtTuycI6BA'
AUDIO_ID_DAY_3 = 'CQACAgIAAxkBAAM6aY34cuQDI_t4lQP72PTW2GUx4HQAAumXAAK2eWFIMv6SAppujOI6BA'
AUDIO_ID_DAY_4 = 'CQACAgIAAxkBAAM7aY36J8-kNf4xaSEbXeJzuCqyU88AAoiYAAK2eWFI5dAtZYosY146BA'
AUDIO_ID_DAY_5 = 'CQACAgIAAxkBAANBaY4WuzylCKIsGFUgjpGUSok8CQADApkAArZ5YUgZ7rCNDynQHzoE'
AUDIO_ID_DAY_6 = 'CQACAgIAAxkBAANDaY4YnMgnuqTDchOwV2_ZLEiJQx4AAh2ZAAK2eWFIC4nHexjIt_U6BA'
AUDIO_ID_DAY_7 = 'CQACAgIAAxkBAANEaY4Zj_jBszCBxeHJt9wcjwby5RYAAmmZAAK2eWFIWptLUuZL8dQ6BA'
DOCUMENT_ID_1 = 'BQACAgIAAxkBAAM8aY4PYg7Qwv499u2dSQToQBba-W8AAkKdAAK2eWFI0nAxkmxWRKY6BA'
DOCUMENT_ID_4 = 'BQACAgIAAxkBAANAaY4VBJORqjW24zn87s4eu-0oH9YAAtuFAAK2eWlI3tBySaISEHo6BA'
DOCUMENT_ID_2 = 'BQACAgIAAxkBAANKaY6hPEeWWyhCsDa8bBJ0zTrX72oAAqqGAAK2eWlIKzuMmrjE_lk6BA'
```

## 📄 `get_project_front.py`

```python

import argparse
import os
from typing import Set, List

# ✅ Расширения файлов
EXTENSIONS: Set[str] = {".py", ".json", ".html", ".css", ".js"}

# ✅ Игнорируемые директории
IGNORED_DIRECTORIES = {
    ".git",
    ".venv",
    "__pycache__",
    ".idea",
    "env",
    "venv",
    "node_modules",
    "site-packages",
    "hooks",
    "logs",
    "refs",
    "pack",
}

DEFAULT_FILES: List[str] = [

]

DEFAULT_DIRS: List[str] = ['.']


EXTENSION_TO_LANG = {
    ".py": "python",
    ".js": "javascript",
    ".json": "json",
    ".html": "html",
    ".css": "css",
}


def read_file_safe(path: str) -> str:
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        try:
            with open(path, encoding="latin-1") as f:
                return f.read()
        except Exception as e:
            return f"[Ошибка чтения (кодировка): {e}]"
    except Exception as e:
        return f"[Ошибка чтения файла: {e}]"


def should_take_file(filename: str) -> bool:
    return os.path.splitext(filename)[1].lower() in EXTENSIONS


def get_lang(filename: str) -> str:
    return EXTENSION_TO_LANG.get(os.path.splitext(filename)[1].lower(), "")


def write_one_file_md(path: str, out, base_dir: str | None = None):
    abs_path = os.path.abspath(path)
    if not os.path.isfile(abs_path):
        out.write(f"\n> ❌ **Файл не найден:** `{abs_path}`\n\n")
        return

    rel_path = os.path.relpath(abs_path, base_dir) if base_dir else path
    lang = get_lang(path)

    out.write(f"\n## 📄 `{rel_path}`\n\n")
    out.write(f"```{lang}\n")
    out.write(read_file_safe(abs_path))
    out.write("\n```\n")


def collect_directory_md(root_dir: str, out):
    root_dir = os.path.abspath(root_dir)

    if not os.path.exists(root_dir):
        out.write(f"\n> ❌ **Папка не найдена:** `{root_dir}`\n\n")
        return

    out.write(f"\n# 📂 Директория: `{root_dir}`\n")

    for current_root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRECTORIES]
        rel_root = os.path.relpath(current_root, root_dir)

        out.write(f"\n## 📁 `{rel_root}`\n")

        for filename in sorted(files):
            if should_take_file(filename):
                full_path = os.path.join(current_root, filename)
                write_one_file_md(full_path, out, root_dir)


def parse_args():
    p = argparse.ArgumentParser(
        description="Собрать файлы и директории в AI-friendly Markdown."
    )

    p.add_argument("--files", "-f", nargs="*", default=DEFAULT_FILES)
    p.add_argument("--dirs", "-d", nargs="*", default=DEFAULT_DIRS)
    p.add_argument("--out", "-o", default="combined_output.md")

    return p.parse_args()


def main():
    args = parse_args()

    with open(args.out, "w", encoding="utf-8") as out:
        out.write("# 🤖 AI Code Bundle\n\n")
        out.write("## 📌 Параметры\n")
        out.write(f"- **Files:** `{args.files}`\n")
        out.write(f"- **Dirs:** `{args.dirs}`\n")
        out.write(f"- **Extensions:** `{sorted(EXTENSIONS)}`\n")

        out.write("\n---\n\n")

        for fpath in args.files:
            write_one_file_md(fpath, out)

        for dpath in args.dirs:
            collect_directory_md(dpath, out)

    print(f"✅ Готово. Markdown файл: {args.out}")


if __name__ == "__main__":
    main()

```

## 📁 `files`

## 📁 `files\1`

## 📁 `files\2`

## 📁 `files\3`

## 📁 `files\4`

## 📁 `files\5`

## 📁 `files\6`

## 📁 `files\7`

## 📁 `tgbot`

## 📄 `tgbot\__init__.py`

```python

```

## 📁 `tgbot\db`

## 📄 `tgbot\db\__init__.py`

```python

```

## 📄 `tgbot\db\crud_users.py`

```python
from datetime import date, datetime, timedelta
from typing import Optional

import pytz
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from tgbot.db.models import UserModel


class UserCrud:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_user(
        self,
        user_id: int,
        user_name: str,
        create_date: Optional[date],
        day: int,
    ):
        user = UserModel(
            user_id=user_id,
            user_name=user_name,
            create_date=create_date,
            day=day,
        )

        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def get_users_list(self):
        result = await self.session.execute(
            select(UserModel)
        )
        return result.scalars().all()

    async def get_user(self, user_id: int):
        result = await self.session.execute(
            select(UserModel).where(UserModel.user_id == user_id)
        )
        return result.scalar_one_or_none()
```

## 📄 `tgbot\db\db.py`

```python
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from config import DB_URL

engine = create_async_engine(DB_URL, future=True, echo=False)

AsyncSessionLocal = async_sessionmaker(
    engine,
    autoflush=False,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

```

## 📄 `tgbot\db\models.py`

```python
from datetime import date
from typing import Optional

from sqlalchemy import Integer, BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from tgbot.db.db import Base


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_name: Mapped[Optional[str]] = mapped_column(String(255))
    user_id: Mapped[int] = mapped_column(
        BigInteger, unique=True, nullable=False
    )

    day : Mapped[int] = mapped_column(Integer)

    create_date : Mapped[Optional[date]] = mapped_column(String)
```

## 📄 `tgbot\db\service.py`

```python

```

## 📁 `tgbot\hadlers`

## 📄 `tgbot\hadlers\__init__.py`

```python

```

## 📄 `tgbot\hadlers\day_1.py`

```python
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



```

## 📄 `tgbot\hadlers\day_2.py`

```python
from aiogram import Router, F, types
from config import AUDIO_ID_DAY_2, DOCUMENT_ID_2
from tgbot.keyboars.user_replay_keyboards import (
    day2_step2_keyboard,
    day2_podcast_keyboard,
    day2_listened_keyboard,
    day2_done_keyboard,
    next_day_test_keyboard
)

router = Router()


# 🔹 Старт дня 2
@router.message(F.text == "/day2")
async def start_day2(message: types.Message):

    # 1️⃣ Первый текст
    with open("files/2/1.txt", encoding="utf-8") as f:
        text1 = f.read()

    await message.answer(text1)

    # 2️⃣ Второй текст + кнопка
    with open("files/2/2.txt", encoding="utf-8") as f:
        text2 = f.read()

    await message.answer(
        text2,
        reply_markup=day2_step2_keyboard()
    )


# 🔹 Кнопка: "Прочитала. Готова делать эти шаги"
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

    await callback.message.answer(
        text,
        reply_markup=day2_podcast_keyboard()
    )

    await callback.answer()


# 🔹 Кнопка: "Слушать подкаст"
@router.callback_query(F.data == "day2_podcast")
async def day2_podcast(callback: types.CallbackQuery):

    await callback.message.answer_audio(
        AUDIO_ID_DAY_2,
        reply_markup=day2_listened_keyboard()
    )

    await callback.answer()


# 🔹 Кнопка: "Прослушала подкаст"
@router.callback_query(F.data == "day2_task")
async def day2_task(callback: types.CallbackQuery):

    # 1️⃣ Текст задания
    with open("files/2/Assignment.txt", encoding="utf-8") as f:
        assignment_text = f.read()

    await callback.message.answer(assignment_text)

    # 2️⃣ Документ + кнопка
    await callback.message.answer_document(
        DOCUMENT_ID_2,
        reply_markup=day2_done_keyboard()
    )

    await callback.answer()


# 🔹 Кнопка: "Сделала практику"
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





```

## 📄 `tgbot\hadlers\day_3.py`

```python
from tgbot.keyboars.user_replay_keyboards import day3_podcast_keyboard, day3_task_keyboard, day3_done_keyboard

from config import AUDIO_ID_DAY_1, AUDIO_ID_DAY_2, AUDIO_ID_DAY_3
from tgbot.keyboars.user_replay_keyboards import day1_next_keyboard, day1_podcast_keyboard, day1_listened_keyboard, \
    day1_video_keyboard, day1_done_keyboard, day2_step1_keyboard, day2_step2_keyboard, day2_podcast_keyboard, \
    day2_listened_keyboard, day2_written_keyboard, day2_done_keyboard

from aiogram import Router, F, types

router = Router()

@router.message(F.text == "/day3")
async def start_day3(message: types.Message):

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

    await message.answer(
        text,
        reply_markup=day3_podcast_keyboard()
    )

@router.callback_query(F.data == "day3_podcast")
async def day3_podcast(callback: types.CallbackQuery):

    await callback.message.answer_audio(
        AUDIO_ID_DAY_3,
        reply_markup=day3_task_keyboard()
    )

    await callback.answer()

@router.callback_query(F.data == "day3_task")
async def day3_task(callback: types.CallbackQuery):

    with open("files/3/1.txt", encoding="utf-8") as f:
        text = f.read()

    await callback.message.answer(
        text,
        reply_markup=day3_done_keyboard()
    )

    await callback.answer()

@router.callback_query(F.data == "day3_done")
async def day3_done(callback: types.CallbackQuery):

    text = (
        "  Отлично. Послушай сегодня приятную музыку, прими ванну "
        "и не забудь проветрить комнату перед сном."
        "Завтра поговорим о том, как избавиться от навязчивых мыслей "
        "о сексе с ним. Нам понадобится пластилин.\n\n"
        "До завтра."
    )

    await callback.message.answer(text)
    await callback.answer()

async def send_day3(bot, user_id):

    with open("files/3/1.txt", encoding="utf-8") as f:
        text = f.read()

    await bot.send_message(
        user_id,
        text,
        reply_markup=day3_step1_keyboard()
    )

```

## 📄 `tgbot\hadlers\day_4.py`

```python
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

```

## 📄 `tgbot\hadlers\day_5.py`

```python
from aiogram import Router, F, types
from config import AUDIO_ID_DAY_5
from tgbot.keyboars.user_replay_keyboards import (
    day5_start_keyboard,
    day5_listened_keyboard,
    day5_task1_done_keyboard,
    day5_done_keyboard
)

router = Router()


@router.message(F.text == "/day5")
async def start_day5(message: types.Message):

    with open("files/5/1.txt", encoding="utf-8") as f:
        text = f.read()

    await message.answer(
        text,
        reply_markup=day5_start_keyboard()
    )


@router.callback_query(F.data == "day5_podcast")
async def day5_podcast(callback: types.CallbackQuery):

    await callback.message.answer_audio(
        AUDIO_ID_DAY_5,
        reply_markup=day5_listened_keyboard()
    )

    await callback.answer()


@router.callback_query(F.data == "day5_task1")
async def day5_task1(callback: types.CallbackQuery):

    with open("files/5/task.txt", encoding="utf-8") as f:
        text = f.read()

    await callback.message.answer(
        text,
        reply_markup=day5_task1_done_keyboard()
    )

    await callback.answer()


@router.callback_query(F.data == "day5_task2")
async def day5_task2(callback: types.CallbackQuery):

    with open("files/5/task2.txt", encoding="utf-8") as f:
        text = f.read()

    await callback.message.answer(
        text,
        reply_markup=day5_done_keyboard()
    )

    await callback.answer()


@router.callback_query(F.data == "day5_done")
async def day5_done(callback: types.CallbackQuery):

    await callback.message.answer(
        "Отлично. Ещё один день пройден. До завтра."
    )

    await callback.answer()

```

## 📄 `tgbot\hadlers\day_6.py`

```python
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

```

## 📄 `tgbot\hadlers\day_7.py`

```python
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

```

## 📄 `tgbot\hadlers\test_tools.py`

```python
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

```

## 📄 `tgbot\hadlers\user.py`

```python

from tgbot.keyboars.user_replay_keyboards import start_keyboard, hesitate_keyboard, pay_only_keyboard, tips_keyboard, \
    pay_or_start_keyboard, day1_next_keyboard

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

```

## 📁 `tgbot\keyboars`

## 📄 `tgbot\keyboars\__init__.py`

```python

```

## 📄 `tgbot\keyboars\user_replay_keyboards.py`

```python
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder



def start_keyboard():
    kb = InlineKeyboardBuilder()

    kb.add(
        InlineKeyboardButton(
            text="Оплатить",
            callback_data="pay"
        )
    )
    kb.add(
        InlineKeyboardButton(
            text="Не могу решиться",
            callback_data="hesitate"
        )
    )

    kb.adjust(1)
    return kb.as_markup()
def hesitate_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(
        InlineKeyboardButton(
            text="Оплатить",
            callback_data="pay"
        )
    )
    kb.add(
        InlineKeyboardButton(
            text="Ещё советы",
            callback_data="more_tips"
        )
    )

    kb.adjust(1)
    return kb.as_markup()


def tips_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(
        InlineKeyboardButton(
            text="Оплатить",
            callback_data="pay"
        )
    )
    kb.add(
        InlineKeyboardButton(
            text="Ещё советы",
            callback_data="final_push"
        )
    )

    kb.adjust(1)
    return kb.as_markup()


def pay_only_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(
        InlineKeyboardButton(
            text="Оплатить",
            callback_data="pay"
        )
    )

    kb.adjust(1)
    return kb.as_markup()

def day1_next_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="Поняла. Далее",
        callback_data="day1_step2"
    ))
    return kb.as_markup()


def day1_podcast_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="Слушать подкаст",
        callback_data="day1_podcast"
    ))
    return kb.as_markup()


def day1_listened_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="Прослушала",
        callback_data="day1_practice"
    ))
    return kb.as_markup()


def day1_video_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="Смотреть видео",
        callback_data="day1_video"
    ))
    return kb.as_markup()


def day1_done_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="Я сделала практику",
        callback_data="day1_done"
    ))
    return kb.as_markup()

def day2_step1_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="Поняла. Следующий шаг?",
        callback_data="day2_step2"
    ))
    return kb.as_markup()


def day2_step2_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="Прочитала. Готова делать эти шаги",
        callback_data="day2_step2"
    ))
    return kb.as_markup()



def day2_podcast_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="Слушать подкаст",
        callback_data="day2_podcast"
    ))
    return kb.as_markup()


def day2_listened_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="Прослушала подкаст",
        callback_data="day2_task"
    ))
    return kb.as_markup()


def day2_written_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="Написала",
        callback_data="day2_assignment"
    ))
    return kb.as_markup()


def day2_done_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="Сделала практику",
        callback_data="day2_done"
    ))
    return kb.as_markup()
def day3_podcast_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="Слушать подкаст",
        callback_data="day3_podcast"
    ))
    return kb.as_markup()


def day3_task_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="Задание «Разочарование»",
        callback_data="day3_task"
    ))
    return kb.as_markup()


def day3_done_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="Я выполнила задание",
        callback_data="day3_done"
    ))
    return kb.as_markup()

def day4_start_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(
        InlineKeyboardButton(
            text="Слушать подкаст",
            callback_data="day4_podcast"
        )
    )
    kb.add(
        InlineKeyboardButton(
            text="Техника «Диафрагма»",
            callback_data="day4_practice"
        )
    )
    kb.adjust(1)
    return kb.as_markup()


def day4_video_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(
        InlineKeyboardButton(
            text="Смотреть видео",
            callback_data="day4_video"
        )
    )
    kb.adjust(1)
    return kb.as_markup()


def day4_done_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(
        InlineKeyboardButton(
            text="Выполнила",
            callback_data="day4_done"
        )
    )
    kb.adjust(1)
    return kb.as_markup()

def day5_start_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(
        InlineKeyboardButton(
            text="Слушать подкаст",
            callback_data="day5_podcast"
        )
    )
    kb.adjust(1)
    return kb.as_markup()


def day5_listened_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(
        InlineKeyboardButton(
            text="Прослушала. Записала",
            callback_data="day5_task1"
        )
    )
    kb.adjust(1)
    return kb.as_markup()


def day5_task1_done_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(
        InlineKeyboardButton(
            text="Задание 1 выполнила",
            callback_data="day5_task2"
        )
    )
    kb.adjust(1)
    return kb.as_markup()


def day5_done_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(
        InlineKeyboardButton(
            text="Выполнила задания",
            callback_data="day5_done"
        )
    )
    kb.adjust(1)
    return kb.as_markup()

def day6_start_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(
        InlineKeyboardButton(
            text="Слушать подкаст",
            callback_data="day6_podcast"
        )
    )
    kb.adjust(1)
    return kb.as_markup()


def day6_listened_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(
        InlineKeyboardButton(
            text="Прослушала подкаст",
            callback_data="day6_task"
        )
    )
    kb.adjust(1)
    return kb.as_markup()


def day6_done_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(
        InlineKeyboardButton(
            text="Выполнила задание",
            callback_data="day6_done"
        )
    )
    kb.adjust(1)
    return kb.as_markup()


def day7_start_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(
        InlineKeyboardButton(
            text="Слушать подкаст",
            callback_data="day7_podcast"
        )
    )
    kb.adjust(1)
    return kb.as_markup()


def day7_task_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(
        InlineKeyboardButton(
            text="Последнее задание",
            callback_data="day7_task"
        )
    )
    kb.adjust(1)
    return kb.as_markup()


def day7_consult_keyboard(url: str):
    kb = InlineKeyboardBuilder()
    kb.add(
        InlineKeyboardButton(
            text="Записаться на консультацию",
            url=url
        )
    )
    kb.adjust(1)
    return kb.as_markup()


def pay_or_start_keyboard():
    kb = InlineKeyboardBuilder()

    kb.add(
        InlineKeyboardButton(
            text="Оплатить",
            callback_data="pay"
        )
    )

    kb.add(
        InlineKeyboardButton(
            text="Начать 1 день",
            callback_data="start_day1_direct"
        )
    )

    kb.adjust(1)
    return kb.as_markup()

```

## 📁 `tgbot\service`

## 📄 `tgbot\service\__init__.py`

```python

```

## 📄 `tgbot\service\day_scheduler.py`

```python
import asyncio
from datetime import datetime, date, time, timedelta

from aiogram import Bot
from sqlalchemy import select

from tgbot.db.db import AsyncSessionLocal
from tgbot.db.models import UserModel
from tgbot.service.sender_content import SenderService


class DayScheduler:

    def __init__(self, bot: Bot, send_time: time):
        self.bot = bot
        self.send_time = send_time

    async def start(self):
        while True:
            await self.wait_until_time()
            await self.process_users()

    async def wait_until_time(self):
        now = datetime.now()
        target = datetime.combine(now.date(), self.send_time)

        if now >= target:
            target += timedelta(days=1)

        sleep_seconds = (target - now).total_seconds()
        await asyncio.sleep(sleep_seconds)

    async def process_users(self):
        async with AsyncSessionLocal() as session:
            result = await session.execute(select(UserModel))
            users = result.scalars().all()

            for user in users:
                service = SenderService(self.bot, session)
                await service.check_and_update_day(user)

```

## 📄 `tgbot\service\payment.py`

```python
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

```

## 📄 `tgbot\service\sender_content.py`

```python

from datetime import date
from aiogram import Bot, types
from sqlalchemy.ext.asyncio import AsyncSession

from tgbot.db.models import UserModel


class SenderService:

    def __init__(self, bot: Bot, session: AsyncSession):
        self.bot = bot
        self.session = session

    async def check_and_update_day(self, user: UserModel):
        if not user.create_date:
            return

        today = date.today()
        passed_days = (today - user.create_date).days + 1
        if passed_days > 7:
            return

        if passed_days > user.day:
            user.day = passed_days
            await self.session.commit()

            await self.send_day_content(user)


```
