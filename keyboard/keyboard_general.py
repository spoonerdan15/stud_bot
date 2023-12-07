from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def kb0():
    kb0 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Куда вы планируете поступать?')
    b2 = KeyboardButton('Как подать документы?')
    b3 = KeyboardButton('Списки подавших документы')
    b4 = KeyboardButton('Позвонить нам')
    b5 = KeyboardButton('Написать нам')
    b6 = KeyboardButton('Написать нам в VK')
    b7 = KeyboardButton('Мы на сайте ВГСПУ')
    b8 = KeyboardButton('Новостной канал Приемной комиссии')
    kb0.add(b1).add(b2).add(b3).add(b4).add(b5).add(b6).add(b7).add(b8)
    return kb0


def kb1():
    kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Бакалавриат/специалитет')
    b2 = KeyboardButton('Магистратура')
    b3 = KeyboardButton('Аспирантура')
    b4 = KeyboardButton('Назад')
    kb1.add(b1).add(b2).add(b3).add(b4)
    return kb1


def kb2():
    kb2 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Личный кабинет ВГСПУ')
    b2 = KeyboardButton('Единый портал государственных услуг')
    b3 = KeyboardButton('Лично')
    b4 = KeyboardButton('Назад')
    kb2.add(b1).add(b2).add(b3).add(b4)
    return kb2


def kb2_1():
    kb2_1 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Назад')
    kb2_1.add(b1)
    return kb2_1


def kb2_2():
    kb2_2 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Назад')
    kb2_2.add(b1)
    return kb2_2


def kb2_3():
    kb2_3 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Назад')
    kb2_3.add(b1)
    return kb2_3


def kb3():
    kb3 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Назад')
    kb3.add(b1)
    return kb3


def kb4():
    kb4 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Назад')
    kb4.add(b1)
    return kb4


def kb5():
    kb5 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Назад')
    kb5.add(b1)
    return kb5


def kb6():
    kb6 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Назад')
    kb6.add(b1)
    return kb6


def kb7():
    kb7 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Назад')
    kb7.add(b1)
    return kb7


def kb8():
    kb8 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Назад')
    kb8.add(b1)
    return kb8


