# Space Telegram
Программа умеет скачивать фотографии на космическую тематику с 3 разных ресурсов и публиковать их с помощью Telegram-бота в Telegram-канал по одной в раз заданное время.

## Окружение
Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3.13/library/venv.html) для изоляции проекта.

### Настройка виртуальное окружение
* Для Windows:
```bash
python -m venv env
venv\Scripts\activate
```
## Зависимости
Python3 должен быть уже установлен. Используйте `pip` или `pip3` для установки зависимостей:
```bash
pip install -r requirements.txt
```
## Переменные окружения

### Как получить
Получите [api key](https://api.nasa.gov) для скачивания фотографий с сайта `NASA`

Ключ необходимо добавить в `.env`, предварительно создав его в корне проекта:
```
NASA_API_KEY='ваш_api_key'
```
Для работы с Telegram-каналом необходимо зарегистрировать своего бота в Telegram с помощью [@BotFather](https://telegram.me/BotFather). После регистрации получите API-токен бота. Токен выглядит примерно так: `958423683:AAEAtJ5Lde5YYfkjergber`

Токен необходимо будет добавить в `.env`:
```
BOT_TOKEN='ваш_токен'
```
## Запуск
### fetch_spacex_images.py
Программа получает фото запуска ракет SpaceX по `id` запуска, например `5eb87d47ffd86e000604b38a`, или последнего запуска по умолчанию.
```bash
python fetch_spacex_images.py --launch_id <launch_id>
```

### fetch_nasa_apod.py
Программа получает фото с сайта NASA из раздела APOD: Astronomy Picture of the Day.
```bash
python fetch_nasa_apod.py
```

### fetch_epic_archive.py
Программа получает фото Земли с сайта NASA из раздела EPIC: Earth Polychromatic Imaging Camera.
```bash
python fetch_epic_archive.py
```

### telegram_bot.py
Telegram-бот, который выбирает рандомно фотографию и всех скаченных ранее и публикует её на Telegram-канале. При вызове программы необходимо указать период времени публикации фото в секундах, например `--time 5`, или, если ничего не указывать, 4 часа по умолчанию.
```bash
python telegram_bot.py <--time>
```

## Примечание

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
