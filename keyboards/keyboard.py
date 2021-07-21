from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
                InlineKeyboardButton, InlineKeyboardMarkup

from config import URL_AFISHA, URL_CLASSIKA, URL_ROCK, URL_POPIT, URL_JAZ, URL_PHONK, URL_SHANSON, URL_RAP, URL_ELECTRO, \
    URL_OTHER, URL_AFISHA1, URL_CLASSIKA1, URL_ROCK1, URL_POPIT1, URL_JAZ1, URL_PHONK1, URL_SHANSON1, URL_RAP1, \
    URL_ELECTRO1, URL_OTHER1, URL_AFISHA2, URL_CLASSIKA2, URL_ROCK2, URL_POPIT2, URL_JAZ2, URL_PHONK2, URL_SHANSON2, \
    URL_RAP2, URL_ELECTRO2, URL_OTHER2

btn_main = KeyboardButton("Главное меню")

# -- Main Menu --
btn1 = KeyboardButton("Кафе/Ресторан")
btn2 = KeyboardButton("Мероприятия")
btn3 = KeyboardButton("Достопримечательности")
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn1, btn2, btn3)


#--cafe--
r1 = InlineKeyboardButton(text="Адмиралтейский", url="https://www.restoclub.ru/spb/search/restorany-rjadom-s-metro-admiraltejskaja")
r2 = InlineKeyboardButton(text="Василеостровский", url="https://www.restoclub.ru/spb/search?expertChoice=false&types%5B%5D=2&types%5B%5D=1&polygons%5B%5D=217")
r3 = InlineKeyboardButton(text="Выборгский", url="https://www.restoclub.ru/spb/search?expertChoice=false&types%5B%5D=2&types%5B%5D=1&polygons%5B%5D=224")
r4 = InlineKeyboardButton(text="Калининский", url="https://www.restoclub.ru/spb/search?expertChoice=false&types%5B%5D=2&types%5B%5D=1&polygons%5B%5D=218")
r5 = InlineKeyboardButton(text="Кировский", url="https://www.restoclub.ru/spb/search?expertChoice=false&types%5B%5D=2&types%5B%5D=1&polygons%5B%5D=219")
r6 = InlineKeyboardButton(text="Колпинский", url="https://www.restoclub.ru/spb/search/restorany-v-kolpino")
r7 = InlineKeyboardButton(text="Красногвардейский", url="https://www.restoclub.ru/spb/search/restorany-kafe-i-bary-v-krasnogvardejskom-rajone")
r8 = InlineKeyboardButton(text="Красносельский", url="https://www.restoclub.ru/spb/search?expertChoice=false&types%5B%5D=2&types%5B%5D=1&polygons%5B%5D=222")
r9 = InlineKeyboardButton(text="Кронштадтский", url="https://www.restoclub.ru/spb/search?expertChoice=false&types%5B%5D=2&types%5B%5D=1&districts%5B%5D=5035")
r10 = InlineKeyboardButton(text="Курортный", url="https://www.restoclub.ru/spb/search/1?expertChoice=false&types%5B%5D=2&types%5B%5D=1&districts%5B%5D=5015")
r11 = InlineKeyboardButton(text="Московский", url="https://www.restoclub.ru/spb/search/1?expertChoice=false&types%5B%5D=2&types%5B%5D=1&polygons%5B%5D=226")
r12 = InlineKeyboardButton(text="Невский", url="https://www.restoclub.ru/spb/search?expertChoice=false&types%5B%5D=2&types%5B%5D=1&polygons%5B%5D=227")
r13 = InlineKeyboardButton(text="Петроградский", url="https://www.restoclub.ru/spb/search?expertChoice=false&types%5B%5D=2&types%5B%5D=1&polygons%5B%5D=228")
r14 = InlineKeyboardButton(text="Петродворцовый", url="https://www.tripadvisor.ru/Restaurants-g2418649-Petrodvortsovy_District_St_Petersburg_Northwestern_District.html")
r15 = InlineKeyboardButton(text="Приморский", url="https://www.restoclub.ru/spb/search?expertChoice=false&types%5B%5D=2&types%5B%5D=1&polygons%5B%5D=230")
r16 = InlineKeyboardButton(text="Пушкинский", url="https://www.restoclub.ru/spb/search/restorany-kafe-i-bary-v-pushkine")
r17 = InlineKeyboardButton(text="Фрунзенский", url="https://www.restoclub.ru/spb/search?expertChoice=false&types%5B%5D=2&types%5B%5D=1&polygons%5B%5D=232")
r18 = InlineKeyboardButton(text="Центральный", url="https://www.restoclub.ru/spb/search?expertChoice=false&types%5B%5D=2&types%5B%5D=1&polygons%5B%5D=296")
r19 = InlineKeyboardButton(text="Отмена", callback_data="cancel")
cafe = InlineKeyboardMarkup(row_width=2).add(r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19)

# --Мероприятия--
btninfo1 = KeyboardButton("Концерт 🎼")
btninfo2 = KeyboardButton("Кино 🎬")
btninfo3 = KeyboardButton("Театр 🎭")
btn2_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btninfo1, btninfo2, btninfo3, btn_main)

#--movie--

r1 = InlineKeyboardButton(text="Боевик", url="https://afisha.yandex.ru/saint-petersburg/cinema?filter=action")
r2 = InlineKeyboardButton(text="Детектив", url="https://afisha.yandex.ru/saint-petersburg/cinema?filter=detective")
r3 = InlineKeyboardButton(text="Драма", url="https://afisha.yandex.ru/saint-petersburg/cinema?filter=drama")
r4 = InlineKeyboardButton(text="Комедия", url="https://afisha.yandex.ru/saint-petersburg/cinema?filter=comedy")
r5 = InlineKeyboardButton(text="Мелодрама", url="https://afisha.yandex.ru/saint-petersburg/cinema?filter=thriller")
r6 = InlineKeyboardButton(text="Приключения", url="https://afisha.yandex.ru/saint-petersburg/cinema?filter=thriller")
r7 = InlineKeyboardButton(text="Триллер", url="https://afisha.yandex.ru/saint-petersburg/cinema?filter=thriller")
r8 = InlineKeyboardButton(text="Ужасы", url="https://afisha.yandex.ru/saint-petersburg/cinema?filter=horror")
r9 = InlineKeyboardButton(text="Фантастика", url="https://afisha.yandex.ru/saint-petersburg/cinema?filter=fiction")
r10 = InlineKeyboardButton(text="Мультфильм", url="https://afisha.yandex.ru/saint-petersburg/cinema?filter=cartoon")
r11 = InlineKeyboardButton(text="Документальный", url="https://afisha.yandex.ru/saint-petersburg/cinema?filter=documentary")
r12 = InlineKeyboardButton(text="Семейное кино", url="https://afisha.yandex.ru/saint-petersburg/cinema?filter=family_movie")
r13 = InlineKeyboardButton(text="Отмена", callback_data="cancel")
cinema = InlineKeyboardMarkup(row_width=2).add(r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13)

# -- theatre --
r1 = InlineKeyboardButton(text="Комедия", url="https://afisha.yandex.ru/saint-petersburg/theatre?filter=comedy")
r2 = InlineKeyboardButton(text="Мюзикл", url="https://afisha.yandex.ru/saint-petersburg/theatre?filter=musical")
r3 = InlineKeyboardButton(text="Балет", url="https://afisha.yandex.ru/saint-petersburg/theatre?filter=ballet")
r4 = InlineKeyboardButton(text="Драма", url="https://afisha.yandex.ru/saint-petersburg/theatre?filter=drama")
r5 = InlineKeyboardButton(text="Опера", url="https://afisha.yandex.ru/saint-petersburg/theatre?filter=opera")
r6 = InlineKeyboardButton(text="Отмена", callback_data="cancel")
theatre = InlineKeyboardMarkup(row_width=1).add(r1, r2, r3, r4, r5, r6)

#--Достопримечательности--
b1 = InlineKeyboardButton(text="Архитектура", url="https://www.culture.ru/architecture/institutes/location-sankt-peterburg")
b2 = InlineKeyboardButton(text="Набережные", url="https://mostotrest-spb.ru/embankments")
b3 = InlineKeyboardButton(text="Исторические места", url="https://walkspb.ru/articles/glav-dostopr")
b4 = InlineKeyboardButton(text="Памятники, скульптуры и мемориалы", url="https://peterburg2.ru/restplaces/379/")
b5 = InlineKeyboardButton(text="Сады и парки", url="https://topparki.ru/parki-skvery-i-sady-sankt-peterburga/")
b6 = InlineKeyboardButton(text="Отмена", callback_data="cancel")
attractions = InlineKeyboardMarkup(row_width=1).add(b1, b2, b3, b4, b5, b6)

#--concerts--
concerts=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Эта неделя", callback_data="date:this"),
            InlineKeyboardButton(text="Следующая неделя", callback_data="date:next")
        ],
        [
            InlineKeyboardButton(text="Без фильтра даты", callback_data="date:without")
        ],
        [
            InlineKeyboardButton(text="Отмена", callback_data="cancel")
        ]
    ]
)
choicejanre2=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Полная афиша", url=URL_AFISHA1),
        ],
        [
            InlineKeyboardButton(text="Классика", url=URL_CLASSIKA1),
            InlineKeyboardButton(text="Рок", url=URL_ROCK1)
        ],
        [
            InlineKeyboardButton(text="Поп/эстрада", url=URL_POPIT1),
            InlineKeyboardButton(text="Джаз", url=URL_JAZ1)
        ],
        [
            InlineKeyboardButton(text="Народное, фолк", url=URL_PHONK1),
            InlineKeyboardButton(text="Шансон", url=URL_SHANSON1),
        ],
        [
            InlineKeyboardButton(text="Хип-хоп, реп", url=URL_RAP1),
            InlineKeyboardButton(text="Электронная", url=URL_ELECTRO1)
        ],
        [
            InlineKeyboardButton(text="Другое", url=URL_OTHER1)
        ],
        [
            InlineKeyboardButton(text="Отмена", callback_data="cancel")
        ]
    ]
)
choicejanre3=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Полная афиша", url=URL_AFISHA2),
        ],
        [
            InlineKeyboardButton(text="Классика", url=URL_CLASSIKA2),
            InlineKeyboardButton(text="Рок", url=URL_ROCK2)
        ],
        [
            InlineKeyboardButton(text="Поп/эстрада", url=URL_POPIT2),
            InlineKeyboardButton(text="Джаз", url=URL_JAZ2)
        ],
        [
            InlineKeyboardButton(text="Народное, фолк", url=URL_PHONK2),
            InlineKeyboardButton(text="Шансон", url=URL_SHANSON2),
        ],
        [
            InlineKeyboardButton(text="Хип-хоп, реп", url=URL_RAP2),
            InlineKeyboardButton(text="Электронная", url=URL_ELECTRO2)
        ],
        [
            InlineKeyboardButton(text="Другое", url=URL_OTHER2)
        ],
        [
            InlineKeyboardButton(text="Отмена", callback_data="cancel")
        ]
    ]
)
choicejanre=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Полная афиша", url=URL_AFISHA),
        ],
        [
            InlineKeyboardButton(text="Классика", url=URL_CLASSIKA),
            InlineKeyboardButton(text="Рок", url=URL_ROCK)
        ],
        [
            InlineKeyboardButton(text="Поп/эстрада", url=URL_POPIT),
            InlineKeyboardButton(text="Джаз", url=URL_JAZ)
        ],
        [
            InlineKeyboardButton(text="Народное, фолк", url=URL_PHONK),
            InlineKeyboardButton(text="Шансон", url=URL_SHANSON),
        ],
        [
            InlineKeyboardButton(text="Хип-хоп, реп", url=URL_RAP),
            InlineKeyboardButton(text="Электронная", url=URL_ELECTRO)
        ],
        [
            InlineKeyboardButton(text="Другое", url=URL_OTHER)
        ],
        [
            InlineKeyboardButton(text="Отмена", callback_data="cancel")
        ]
    ]
)
