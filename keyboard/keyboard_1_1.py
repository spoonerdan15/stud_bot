from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def kb1_1():
    kb1_1 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Профили и количество мест')
    b2 = KeyboardButton('Календарь приема')
    b3 = KeyboardButton('Документы для поступления')
    b4 = KeyboardButton('ЕГЭ или вступительные испытания?')
    b5 = KeyboardButton('Особые права и отдельная квота (ссылка на страницу на сайте)')
    b6 = KeyboardButton('Абитуриентам, поступающим по целевым договорам')
    b7 = KeyboardButton('Индивидуальные достижения (ссылка на файл на сайте)')
    b8 = KeyboardButton('ПОДАТЬ ДОКУМЕНТЫ')
    b9 = KeyboardButton('Нет нужной информации? Свяжитесь с нами!')
    b10 = KeyboardButton('Назад')
    kb1_1.add(b1).add(b2).add(b3).add(b4).add(b5).add(b6).add(b7).add(b8).add(b9).add(b10)
    return kb1_1


def kb1_1_1():
    kb1_1_1 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Назад')
    kb1_1_1.add(b1)
    return kb1_1_1


def kb1_1_2():
    kb1_1_2 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Назад')
    kb1_1_2.add(b1)
    return kb1_1_2


def kb1_1_3():
    kb1_1_3 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Перечень документов (https://vgpu.org/prcom/13283)')
    b2 = KeyboardButton('Остались вопросы? Позвоните нам! (+79050616417)')
    b3 = KeyboardButton('Назад')
    kb1_1_3.add(b1).add(b2).add(b3)
    return kb1_1_3


def kb1_1_4():
    kb1_1_4 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Минимальные баллы для подачи документов (ссылка на файл на сайте)')
    b2 = KeyboardButton('Кто имеет право сдавать экзамены?')
    b3 = KeyboardButton('Расписание вступительных испытаний')
    b4 = KeyboardButton('Остались вопросы? Позвоните нам! (+79050616417)')
    b5 = KeyboardButton('Назад')
    kb1_1_4.add(b1).add(b2).add(b3).add(b4).add(b5)
    return kb1_1_4


def kb1_1_5():
    kb1_1_5 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Особые права (ссылка)')
    b2 = KeyboardButton('Отдельная квота (ссылка)')
    b3 = KeyboardButton('Остались вопросы? Позвоните нам! (+79050616417)')
    b4 = KeyboardButton('Назад')
    kb1_1_5.add(b1).add(b2).add(b3).add(b4)
    return kb1_1_5


def kb1_1_6():
    kb1_1_6 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Назад')
    kb1_1_6.add(b1)
    return kb1_1_6


def kb1_1_7():
    kb1_1_7 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Назад')
    kb1_1_7.add(b1)
    return kb1_1_7


def kb1_1_8():
    kb1_1_8 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Как подать документы?')
    b2 = KeyboardButton('Назад')
    kb1_1_8.add(b1).add(b2)
    return kb1_1_8