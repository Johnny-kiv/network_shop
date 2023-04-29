from aiogram import Bot, Dispatcher, types,executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
insert = KeyboardButton("insert")
cancel = KeyboardButton("cancel")
mainM = ReplyKeyboardMarkup(resize_keyboard=True).add(insert)
bot = Bot(token='6021724545:AAHY5UvQ2ttRGnazCJH2ZlVXI_oORAZbnIA')

# Don't forget to use storage, otherwise answers won't be saved.
# You can find all supported storages here:
# https://github.com/aiogram/aiogram/tree/dev-2.x/aiogram/contrib/fsm_storage
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class Form(StatesGroup):
    name = State()
    price = State()
    image = State()


@dp.message_handler(commands=['start'],state="*")
async def start(mes: types.Message):
    await bot.send_message(mes.from_user.id,text="HI",reply_markup=mainM)
@dp.message_handler()
async def a(mes:types.Message):
    await bot.download(
        mes.photo[-1],
        destination=f"/home/user/imgs{mes.photo[-1].file_id}.png"
    )
executor.start_polling(dp,skip_updates=True)