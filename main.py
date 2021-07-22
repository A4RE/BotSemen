#!venv/bin/python

import logging

from aiogram import Bot, Dispatcher, executor
from aiogram import types
from aiogram.types import CallbackQuery, InputFile, message


from config import TOKEN
from keyboards.keyboard import mainMenu, btn2_menu, cafe, cinema, attractions, \
    concerts, choicejanre, choicejanre3, choicejanre2, theatre

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


# Реакция на команду start
@dp.message_handler(commands=['start'])
async def cmd_answer(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Привет {0.first_name},меня зовут Бот Семен 🐵\n"
                           "Я помогу тебе найти места, где можно классно провести время\n"
                           "Выбери, что тебя интересует из клавиатуры, дальше расскажу, что делать\nДля помощи воспользуйся командой /help".format(message.from_user), reply_markup=mainMenu, parse_mode="MarkdownV2")
    p = open("bot.gif", "rb")
    await bot.send_animation(message.from_user.id, p)

# Реакции на команду help
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, "Вот список команд, которые доступны тебе:\n"
                                                 "/cafe\n/cinema\n/theatre\n/concert\n/attractions")
# cafe
@dp.message_handler(commands=['cafe'])
async def cafe1(message: types.Message):
    await bot.send_message(message.from_user.id, "Выбери район и я отправлю тебе ссылку на топ мест района:", reply_markup=cafe)

# cinema
@dp.message_handler(commands=['cinema'])
async def cinema1(message: types.Message):
    await bot.send_message(message.from_user.id, "Выбери жанр:", reply_markup=cinema)


# theatre
@dp.message_handler(commands=['theatre'])
async def theatre1(message: types.Message):
    await bot.send_message(message.from_user.id, "Выбери жанр:", reply_markup=theatre)


#attractions
@dp.message_handler(commands=['attractions'])
async def theatre1(message: types.Message):
    await bot.send_message(message.from_user.id, "Выбери пунки:", reply_markup=attractions)

# concert
@dp.message_handler(commands=['concert'])
async def concert1(message: types.Message):
    await bot.send_message(message.from_user.id, "Выбери жанр:", reply_markup=concerts)

# обычное взаимодействие
@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == "Кафе/Ресторан":
        await bot.send_message(message.from_user.id, "Выберете район, бот отправит ссылку на топ мест района:", reply_markup=cafe)
    elif message.text == "Главное меню":
        await bot.send_message(message.from_user.id, " Добро пожаловать в главное меню", reply_markup=mainMenu)
    elif message.text == "Мероприятия":
        await bot.send_message(message.from_user.id, "Выбери пункт, а я пришлю тебе варианты 🙂:", reply_markup=btn2_menu)
    elif message.text == "Кино 🎬":
        await bot.send_message(message.from_user.id, "Выбери пункт, а я пришлю тебе варианты 🙂:", reply_markup=cinema)
    elif message.text == "Концерт 🎼":
        await bot.send_message(message.from_user.id, "Выберете пункт:", reply_markup=concerts)
    elif message.text == "Театр 🎭":
        await bot.send_message(message.from_user.id, "Выберете жанр:", reply_markup=theatre)
    elif message.text == "Достопримечательности":
        await bot.send_message(message.from_user.id, "Выбери то, что тебя интересует:", reply_markup=attractions)

@dp.callback_query_handler(text_contains="this")
async def this_concert(call: CallbackQuery):
    await call.message.answer("Перед Вами жанры концертов на этой неделе.\n"
                                "Пожалуйста, выберите нужный.",
                              reply_markup=choicejanre2)

@dp.callback_query_handler(text_contains="next")
async def next_concert(call: CallbackQuery):
    await call.message.answer("Перед Вами жанры концертов на следующей неделе.\n"
                                  "Пожалуйста, выберите нужный.",
                                  reply_markup=choicejanre3)

@dp.callback_query_handler(text_contains="without")
async def without_concert(call: CallbackQuery):
   await call.message.answer("Перед Вами жанры концертов.\n"
                                      "Пожалуйста выберите нужный.",
                                      reply_markup=choicejanre)

@dp.callback_query_handler(text_contains="cancel")
async def cancel_concert(call: CallbackQuery):
    await call.answer("Возврат в общее меню", show_alert=True)
    await call.message.answer("Перед вами главное меню.\n"
                              "Пожалуйста, выберите нужную опцию",
                              reply_markup=mainMenu)

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
