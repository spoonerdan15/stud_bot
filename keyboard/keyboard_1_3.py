from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def kb1_3():
    kb1_3 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Научные специальности (ссылка на страницу сайта)')
    b2 = KeyboardButton('Сроки приема (ссылка на страницу сайта)')
    b3 = KeyboardButton('Документы для поступления (ссылка на страницу сайта)')
    b4 = KeyboardButton('Вступительные испытания (ссылка на страницу сайта)')
    b5 = KeyboardButton('Индивидуальные достижения (ссылка на страницу сайта)')
    b6 = KeyboardButton('ПОДАТЬ ДОКУМЕНТЫ')
    b7 = KeyboardButton('Назад')
    kb1_3.add(b1).add(b2).add(b3).add(b4).add(b5).add(b6).add(b7)
    return kb1_3