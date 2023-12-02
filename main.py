from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton,InlineKeyboardMarkup
import traceback
import _json

from config import *
from keyboard.keyboard_general import *
from keyboard.keyboard_1_1 import *
from keyboard.keyboard_1_2 import *
from keyboard.keyboard_1_3 import *


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

prew = []


@dp.message_handler(commands=['start'])
async def answer_0(message: types.message):
    global prew
    prew.clear()
    stak = format(traceback.extract_stack()[-1][-2][7:])
    prew.append(stak)
    await bot.send_message(chat_id=message.from_user.id,
                           text="Вы начали работу бота",
                           reply_markup=kb0())#клавиатура



@dp.message_handler(text='Куда вы планируете поступать?')
async def answer_1(message: types.message):
    global prew
    stak = format(traceback.extract_stack()[-1][-2][7:])
    prew.append(stak)
    await bot.send_message(chat_id=message.from_user.id,
                           text="Куда вы планируете поступать?",
                           reply_markup=kb1())



@dp.message_handler(text='Бакалавриат/специалитет')
async def answer_1_1(message: types.message):
    global prew
    stak = format(traceback.extract_stack()[-1][-2][7:])
    prew.append(stak)
    await bot.send_message(chat_id=message.from_user.id,
                           text="Что вас интересует?",
                           reply_markup=kb1_1())

@dp.message_handler(text='Профили и количество мест')
async def answer_1_1_1(message: types.message):
    global prew
    stak = format(traceback.extract_stack()[-1][-2][7:])
    prew.append(stak)
    await bot.send_message(chat_id=message.from_user.id,
                           text="ТЕКСТ С ССЫЛКАМИ НА САЙТ",
                           reply_markup=kb1_1_1())


@dp.message_handler(text='Календарь приема')
async def answer_1_1_2(message: types.message):
    global prew
    stak = format(traceback.extract_stack()[-1][-2][7:])
    prew.append(stak)
    await bot.send_message(chat_id=message.from_user.id,
                           text="ТЕКСТ С ССЫЛКОЙ НА САЙТ",
                           reply_markup=kb1_1_2())


@dp.message_handler(text='Документы для поступления')
async def answer_1_1_3(message: types.message):
    global prew
    stak = format(traceback.extract_stack()[-1][-2][7:])
    prew.append(stak)
    await bot.send_message(chat_id=message.from_user.id,
                           text="ТЕКСТ С ССЫЛКОЙ НА САЙТ",
                           reply_markup=kb1_1_3())


@dp.message_handler(text='ЕГЭ или вступительные испытания?')
async def answer_1_1_4(message: types.message):
    global prew
    stak = format(traceback.extract_stack()[-1][-2][7:])
    prew.append(stak)
    await bot.send_message(chat_id=message.from_user.id,
                           text="ТЕКСТ С ССЫЛКОЙ НА САЙТ",
                           reply_markup=kb1_1_4())


@dp.message_handler(text='Особые права и отдельная квота (ссылка на страницу на сайте)')
async def answer_1_1_5(message: types.message):
    global prew
    stak = format(traceback.extract_stack()[-1][-2][7:])
    prew.append(stak)
    await bot.send_message(chat_id=message.from_user.id,
                           text="ТЕКСТ С ССЫЛКОЙ НА САЙТ",
                           reply_markup=kb1_1_5())


@dp.message_handler(text='Абитуриентам, поступающим по целевым договорам')
async def answer_1_1_6(message: types.message):
    global prew
    stak = format(traceback.extract_stack()[-1][-2][7:])
    prew.append(stak)
    await bot.send_message(chat_id=message.from_user.id,
                           text="ТЕКСТ С ССЫЛКОЙ (https://vgpu.org/node/7892) ",
                           reply_markup=kb1_1_6())


@dp.message_handler(text='Индивидуальные достижения (ссылка на файл на сайте)')
async def answer_1_1_7(message: types.message):
    global prew
    stak = format(traceback.extract_stack()[-1][-2][7:])
    prew.append(stak)
    await bot.send_message(chat_id=message.from_user.id,
                           text="ТЕКСТ С ССЫЛКОЙ",
                           reply_markup=kb1_1_7())


@dp.message_handler(text='ПОДАТЬ ДОКУМЕНТЫ')
async def answer_1_1_8(message: types.message):
    global prew
    stak = format(traceback.extract_stack()[-1][-2][7:])
    prew.append(stak)
    await bot.send_message(chat_id=message.from_user.id,
                           text="ТЕКСТ С ССЫЛКОЙ НА ШАГ 2 ",
                           reply_markup=kb1_1_8())


@dp.message_handler(text='Магистратура')
async def answer_1_2(message: types.message):
    global prew
    stak = format(traceback.extract_stack()[-1][-2][7:])
    prew.append(stak)

    await bot.send_message(chat_id=message.from_user.id,
                           text="Что вас интересует?",
                           reply_markup=kb1_2())


@dp.message_handler(text='Программы и количество мест (ссылка на файл на сайте)')
async def answer_1_2_1(message: types.message):
    global prew
    stak = format(traceback.extract_stack()[-1][-2][7:])
    prew.append(stak)
    await bot.send_message(chat_id=message.from_user.id,
                           text="ТЕКСТ С ССЫЛКАМИ НА САЙТ",
                           reply_markup=kb1_2_1())


@dp.message_handler(text='Календарь приема (ссылка на страницу сайте)')
async def answer_1_2_2(message: types.message):
    global prew
    stak = format(traceback.extract_stack()[-1][-2][7:])
    prew.append(stak)
    await bot.send_message(chat_id=message.from_user.id,
                           text="ТЕКСТ С ССЫЛКАМИ НА САЙТ",
                           reply_markup=kb1_2_2())


@dp.message_handler(text='Документы для поступления')
async def answer_1_2_3(message: types.message):
    global prew
    stak = format(traceback.extract_stack()[-1][-2][7:])
    prew.append(stak)
    await bot.send_message(chat_id=message.from_user.id,
                           text="ТЕКСТ С ОБЪЯСНЕНИЕМ ВЫБОРА:",
                           reply_markup=kb1_2_3())


@dp.message_handler(text='Вступительные испытания')
async def answer_1_2_4(message: types.message):
    global prew
    stak = format(traceback.extract_stack()[-1][-2][7:])
    prew.append(stak)
    await bot.send_message(chat_id=message.from_user.id,
                           text="ТЕКСТ С СЫЛКОЙ НА САЙТ",
                           reply_markup=kb1_2_4())


@dp.message_handler(text='Индивидуальные достижения (ссылка на файл на сайт) ')
async def answer_1_2_5(message: types.message):
    global prew
    stak = format(traceback.extract_stack()[-1][-2][7:])
    prew.append(stak)
    await bot.send_message(chat_id=message.from_user.id,
                           text="ТЕКСТ С ССЫЛКОЙ",
                           reply_markup=kb1_2_5())


@dp.message_handler(text='Абитуриентам, поступающим по целевым договорам (https://vgpu.org/node/7892)')
async def answer_1_2_6(message: types.message):
    global prew
    stak = format(traceback.extract_stack()[-1][-2][7:])
    prew.append(stak)
    await bot.send_message(chat_id=message.from_user.id,
                           text="ТЕКСТ С ССЫЛКОЙ (https://vgpu.org/node/7892)",
                           reply_markup=kb1_2_6())


@dp.message_handler(text='ПОДАТЬ ДОКУМЕНТЫ')
async def answer_1_2_7(message: types.message):
    global prew
    stak = format(traceback.extract_stack()[-1][-2][7:])
    prew.append(stak)
    await bot.send_message(chat_id=message.from_user.id,
                           text="ТЕКСТ С ССЫЛКОЙ НА ШАГ 2",
                           reply_markup=kb1_2_7())


@dp.message_handler(text='Аспирантура')
async def answer_1_3(message: types.message):
    global prew
    stak = format(traceback.extract_stack()[-1][-2][7:])
    prew.append(stak)
    await bot.send_message(chat_id=message.from_user.id,
                           text="Что вас интересует?",
                           reply_markup=kb1_3())


@dp.message_handler(text='Как подать документы?')
async def answer_2(message: types.message):
    global prew
    stak = format(traceback.extract_stack()[-1][-2][7:])
    prew.append(stak)
    await bot.send_message(chat_id=message.from_user.id,
                           text="Что вас интересует?",
                           reply_markup=kb2())


@dp.message_handler(text='Назад')
async def answer_back(message: types.message):
    global prew
    code_kb = 'kb' + prew[-2] + '()'
    kb = eval(code_kb)
    prew = prew[:-1]
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы вернулись назад',
                           reply_markup=kb)


if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)