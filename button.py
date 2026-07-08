from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

def get_main_vd() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Matematika🧮"), KeyboardButton(text="Jismoniy tarbiya🏃")],
            [KeyboardButton(text="Informatika💻")]
        ],
        resize_keyboard=True
    )
    return builder

def get_course_vd() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Shaxmat ♟", callback_data="togarak_Shaxmat"))
    builder.add(InlineKeyboardButton(text="Informatika 💻", callback_data="togarak_Informatika"))
    builder.add(InlineKeyboardButton(text="Matematika 🧮", callback_data="togarak_Matematika"))
    builder.add(InlineKeyboardButton(text="Musiqa 🎵", callback_data="togarak_Musiqa"))
    builder.adjust(2)
    return builder.as_markup()

def baho_mezoni() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Qoniqarsiz 👎", callback_data="qoniqarsiz_baho"))
    builder.add(InlineKeyboardButton(text="Qoniqarli 👍", callback_data="qoniqarli_baho"))
    builder.add(InlineKeyboardButton(text="A'lo ⭐", callback_data="alo_baho"))
    builder.adjust(1)
    return builder.as_markup()

def sayt_tugma() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Kanalga o'tish 🚀", url="https://t.me/Yusufbe20_09"))
    return builder.as_markup()
