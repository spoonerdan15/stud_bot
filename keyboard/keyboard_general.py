from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def kb0():
    kb0 = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Куда вы планируете поступать?')
    b2 = KeyboardButton('Как подать документы?')
    b3 = KeyboardButton('Списки подавших документы')
    b4 = KeyboardButton('Позвонить нам (+79050616417)')
    b5 = KeyboardButton('Написать нам (prcom@vspu.ru)')
    b6 = KeyboardButton('Написать нам в VK (https://vk.com/prcomvspu)')
    b7 = KeyboardButton('Мы на сайте ВГСПУ (https://vgpu.org/abitur)')
    b8 = KeyboardButton('Часто задаваемые вопросы (https://vgpu.org/prcom/faq)')
    b9 = KeyboardButton('Новости Приемной комиссии (канал telegram)')
    kb0.add(b1).add(b2).add(b3).add(b4).add(b5).add(b6).add(b7).add(b8).add(b9)
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
    b1 = KeyboardButton('Личный кабинет ВГСПУ (https://abiturient.vspu.ru/)')
    b2 = KeyboardButton('Единый портал государственных услуг (https://www.gosuslugi.ru/)')
    b3 = KeyboardButton('Лично (https://vgpu.org/abitur)')
    b4 = KeyboardButton('Назад')
    kb2.add(b1).add(b2).add(b3).add(b4)
    return kb2