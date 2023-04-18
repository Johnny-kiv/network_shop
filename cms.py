from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
import sqlite3
insert = KeyboardButton("insert")
select = KeyboardButton("select")
mainM = ReplyKeyboardMarkup(resize_keyboard=True).add(insert,select)
bot = Bot(token="6021724545:AAHY5UvQ2ttRGnazCJH2ZlVXI_oORAZbnIA")
dp = Dispatcher(bot=bot)
conn = sqlite3.connect("tovary.db")
cur = conn.cursor()
global flag
flag = 2
@dp.message_handler(commands=['start'])
async def start(mes: types.Message):
    await bot.send_message(mes.from_user.id,text=f"Здравствуйте {mes.from_user.first_name}! Добро пожаловать в компанию Барахолка. Мы предстовляем собой интернет магазмн. Здесь каждый может стать продавцом и продовая все что хочет (кроме оружия). Так что начните свой бизнес здесь! Безопасно удобно и выгодно. Удачи!",reply_markup=mainM)
@dp.message_handler()
async def handler1(mes: types.Message):
    global name, flag
    if mes.text == "insert":
        if flag==2:
            await bot.send_message(mes.from_user.id, "Введите название товара:", reply_markup=mainM)
            flag = 0
@dp.message_handler()
async def handler2(mes: types.Message):
    global price, flag, name
    if flag==0:
        await bot.send_message(mes.from_user.id, "Введите цену товара:", reply_markup=mainM)
        name = mes.text
        flag = 1

@dp.message_handler()
async def handler3(mes: types.Message):
    global price, flag, name
    if flag==1:
        price = mes.text
        flag = 2
    data = [name, price, None,None]
    cur.execute("INSERT INTO Tovary VALUES(?, ?, ?,?);", data)
    conn.commit()
executor.start_polling(dp,skip_updates=True)