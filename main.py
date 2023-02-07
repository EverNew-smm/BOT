import aiogram.utils.exceptions
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

import config
from config import TOKEN_API
from keyboards import kb, urlkb, falkb, culkb


bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot=bot)

HELP_COMMAND = """
<b>/Help</b> - <em>список доступних команд</em>
<b>/Start</b> - <em>запуск бота</em>
<b>/Description</b> - <em>опис бота</em>
<b>/SocialNetworks</b> - <em>Посилання на мої соц мережі</em>
"""

SOCIAL_NETWORKS = """
Telegram = 'https://t.me/Yota3103' 
"""

flag = False


async def on_startup(_):
    print('Бот Запустився!')

@dp.message_handler(Text(equals="Головне меню"))
async def open_kb(message: types.Message):
    await message.answer(text='Вітаю в головному менню!',
                         reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(text='Вітаю у моєму боті по Smm Франшизі! 🐝',
                         reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['Description'])
async def cmd_help(message: types.Message):
    await message.answer(text='У цьому телеграм каналі ти можеш быльше дізнатись про Smm франшизу та придбати один з трьох доступних пакетів: 1) Хочу бомбити , 2) Швидкий старт , 3) Ва-Банк . Більше про них можеш дізнатись натиснувши на них у клавіатурі знизу !')
    await message.delete()

@dp.message_handler(commands=['Хочу-бомбити'])
async def open_urlkb(message: types.Message):
    await message.answer(text='Це перший пакет у данному списку . Ціна цього пакету : 350 грн . (детальніше про нього трохи нижче)',
                         reply_markup=urlkb)
    await message.delete()

@dp.message_handler(commands=['Швидкий-старт'])
async def open_falkb(message: types.Message):
    await message.answer(text='Другий Smm пакет , у даному списку . Ціна 2-го пакету : 590 грн . (детальне про данний пакет , трохи нижче)',
                         reply_markup=falkb)
    await message.delete()

@dp.message_handler(commands=['Ва-Банк'])
async def open_culkb(message: types.Message):
    await message.answer(text='Третій та останій пакет з данного списку . Ціна цього Smm пакету : 1100 грн . (детальніше про цей , самий кращий пакет дляшвидкого страту трохи нижче) ',
                         reply_markup=culkb)
    await message.delete()

@dp.message_handler(commands=['SocialNetworks'])
async def cmd_help(message: types.Message):
    await message.answer(text=SOCIAL_NETWORKS,
                         parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    await message.answer(text=HELP_COMMAND,
                         parse_mode='HTML')
    await message.delete()

PRICE = types.LabeledPrice(label='Настоящая Машина Времени', amount=42000)

@dp.message_handler(commands=['terms'])
async def process_terms_command(message: types.Message):
    await message.reply(MESSAGES['terms'], reply=False)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)