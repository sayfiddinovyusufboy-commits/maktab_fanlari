from aiogram import Dispatcher, Bot, F
from aiogram.types import Message, CallbackQuery
import asyncio
from aiogram.filters import CommandStart, Command
from button import get_main_vd, get_course_vd, baho_mezoni, sayt_tugma

# BotFather'dan yangi token olib, eskisini butunlay o'chirib, o'rniga qo'ying!
token = "8614571874:AAFTaG4o9Rk7r8wKl6MaRgMztdEveWgeA9I"
bot = Bot(token=token)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        f"assalomu aleykum {message.chat.full_name}\n"
        f"kerakli tugmani tanlang👇", reply_markup=get_main_vd()
    )

@dp.message(Command("admin"))
async def admin(message: Message):
    await message.reply("admin:@Yusufbe20_09")

@dp.message(F.text == "Matematika🧮")
async def Maktab(message: Message):
    await message.answer("qiziqarli fan tanladingiz😊")

@dp.message(F.text == "Jismoniy tarbiya🏃")
async def togaraklar(message: Message):
    await message.answer("Togaraklar", reply_markup=get_course_vd())

@dp.callback_query(F.data.startswith("togarak"))
async def inline_togarak(call: CallbackQuery):
    data = call.data
    togarak_nomi = data.split("_")[1]
    await call.message.answer(
        f"siz {togarak_nomi} togaragini tanladingiz 👌\n"
        f"bu togaragimizni baholang", reply_markup=baho_mezoni()
    )

@dp.callback_query(F.data.endswith("baho"))
async def inline_baho(call: CallbackQuery):
    data = call.data
    baho = data.split("_")[0]
    
    if baho == "qoniqarsiz":
        await call.answer("togaragimiz yoqmagan bolsa uzr", show_alert=True)
        await call.message.delete()
    elif baho == "qoniqarli":
        await call.message.reply("baho uchun raxmat🫡")
    elif baho == "alo":
        await call.message.edit_text("tashakkur😊")

@dp.message(F.text == "Informatika💻")
async def Informatika(message: Message):
    await message.answer("bizning kanalimiz👌", reply_markup=sayt_tugma())

async def main():
    print("bot ishga tushdi")
    await dp.start_polling(bot)

asyncio.run(main())
