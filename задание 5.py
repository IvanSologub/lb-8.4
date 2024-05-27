#Задача №5
#В код добавлен словарь DATABASE, в нём хранятся данные о том, кто из друзей где живёт.

#Напишите код функции what_time(), которая по имени друга скажет, сколько у него сейчас времени.

import datetime as dt

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь'
}

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2
}

def what_time(friend):
    city = DATABASE.get(friend)
    if city is not None:
        utc_offset = UTC_OFFSET.get(city)
        if utc_offset is not None:
            utc_time = dt.datetime.utcnow()
            local_time = utc_time + dt.timedelta(hours=utc_offset)
            return local_time.strftime('%H:%M:%S')
        else:
            return 'Не удалось определить поправку к UTC для города друга.'
    else:
        return 'Город друга не найден в базе данных.'

print(what_time('Соня'))