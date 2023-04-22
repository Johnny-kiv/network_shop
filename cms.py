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
async def handler(mes: types.Message):
    """Conversation entrypoint"""
    if mes.text == "insert":

        # Set state
        await Form.name.set()
        await mes.reply("Введите имя товара:",reply_markup=mainM)

# You can use state='*' if you want to handle all states
@dp.message_handler(state='*', commands=['cancel'])
async def cancel_handler(mes: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await mes.reply('Cancelled.',reply_markup=mainM)


@dp.message_handler(state=Form.name)
async def process_name(mes: types.Message, state: FSMContext):
    await state.finish()
    global name
    name = mes.text
    await Form.price.set()
    await mes.reply("Введите цену товара:",reply_markup=mainM)  # <-- Here we get the name

@dp.message_handler(state=Form.price)
async def process_price(message: types.Message, state: FSMContext):
    await state.finish()
    global name,summa
    summa = message.text
    await message.reply("Пришлите изображение:",reply_markup=mainM)  # <-- Here we get the name

@dp.message_handler(state=Form.image)
async def process_image(message: types.Message, state: FSMContext):
    await state.finish()
    global name,summa,image
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    await message.reply(f"Товар: {name}\n Сумма: {summa}",reply_markup=mainM)  # <-- Here we get the name
executor.start_polling(dp,loop=True,skip_updates=True)