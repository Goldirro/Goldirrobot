from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

BOT_TOKEN = "7567682977:AAEM2cmYxVtVgqD14Kcmuwp8NhCwdWxKYCo"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("🎬 Assalom alaykum! @GoldirroKinoBot xizmatda.")

@dp.message_handler(lambda msg: msg.text.startswith("#"))
async def kino_qidiruv(message: types.Message):
    kod = message.text.strip()
    if kod == "#101":
        await message.answer("🎞 Kino: ChatGPT do‘stim\n📥 Yuklab olish: [kino fayli]")
    else:
        await message.answer("❌ Bunday koddagi kino topilmadi.")

if __name__ == "__main__":
    executor.start_polling(dp)