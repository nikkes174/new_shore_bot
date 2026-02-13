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

def payment_confirm_keyboard():
    kb = InlineKeyboardBuilder()

    kb.add(
        InlineKeyboardButton(
            text="Перейти к оплате",
            callback_data="create_payment"
        )
    )

    kb.adjust(1)
    return kb.as_markup()
