from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='/Start')
b2 = KeyboardButton(text='/Description')
b3 = KeyboardButton(text='/Хочу-бомбити')
b4 = KeyboardButton(text='/Швидкий-старт')
b5 = KeyboardButton(text='/Ва-Банк')
b6 = KeyboardButton(text='/SocialNetworks')
b7 = KeyboardButton(text='/help')

kb.add(b1).add(b2).add(b3, b4, b5).add(b6).add(b7)


urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='Що входить в данний пакет', url='https://skillbox.ru/code/')
urlButton2 = InlineKeyboardButton(text='Придбати', url='https://skillbox.ru/code/')
urlButton3 = InlineKeyboardButton(text='Є питання напиши мені', url='https://t.me/Den1uc')
urlkb.add(urlButton,urlButton2,urlButton3)

falkb = InlineKeyboardMarkup(row_width=1)
falButton = InlineKeyboardButton(text='Що входить в данний пакет', url='https://skillbox.ru/media/code/')
falButton2 = InlineKeyboardButton(text='Придбати', url='https://skillbox.ru/code/')
falButton3 = InlineKeyboardButton(text='Є питання напиши мені', url='https://t.me/Den1uc')
falkb.add(falButton,falButton2,falButton3)

culkb = InlineKeyboardMarkup(row_width=1)
culButton = InlineKeyboardButton(text='Що входить в данний пакет', url='https://skillbox.ru/media/code/')
culButton2 = InlineKeyboardButton(text='Придбати', url='https://skillbox.ru/code/')
culButton3 = InlineKeyboardButton(text='Є питання апиши мені', url='https://t.me/Den1uc')
culkb.add(culButton,culButton2,culButton3)



