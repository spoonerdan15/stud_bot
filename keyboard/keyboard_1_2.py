from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def kb1_2():
    kb1_2 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Программы и количество мест (ссылка на файл на сайте)')
    b2 = KeyboardButton('Календарь приема (ссылка на страницу сайте)')
    b3 = KeyboardButton('Документы для поступления')
    b4 = KeyboardButton('Вступительные испытания')
    b5 = KeyboardButton('Индивидуальные достижения (ссылка на файл на сайт) ')
    b6 = KeyboardButton('Абитуриентам, поступающим по целевым договорам (https://vgpu.org/node/7892)')
    b7 = KeyboardButton('ПОДАТЬ ДОКУМЕНТЫ')
    b8 = KeyboardButton('Нет нужной информации? Свяжитесь с нами!')
    b9 = KeyboardButton('Назад')
    kb1_2.add(b1).add(b2).add(b3).add(b4).add(b5).add(b6).add(b7).add(b8).add(b9)
    return kb1_2


def kb1_2_1():
    kb1_2_1 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Назад')
    kb1_2_1.add(b1)
    return kb1_2_1


def kb1_2_2():
    kb1_2_2 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Назад')
    kb1_2_2.add(b1)
    return kb1_2_2


def kb1_2_3():
    kb1_2_3 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Перечень документов (https://vgpu.org/prcom/13283)')
    b2 = KeyboardButton('Остались вопросы? (+79050616417)')
    b3 = KeyboardButton('Назад')
    kb1_2_3.add(b1).add(b2).add(b3)
    return kb1_2_3


def kb1_2_4():
    kb1_2_4 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Назад')
    kb1_2_4.add(b1)
    return kb1_2_4


def kb1_2_5():
    kb1_2_5 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Назад')
    kb1_2_5.add(b1)
    return kb1_2_5


def kb1_2_6():
    kb1_2_6 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Назад')
    kb1_2_6.add(b1)
    return kb1_2_6


def kb1_2_7():
    kb1_2_7 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Как подать документы?')
    b2 = KeyboardButton('Назад')
    kb1_2_7.add(b1).add(b2)
    return kb1_2_7