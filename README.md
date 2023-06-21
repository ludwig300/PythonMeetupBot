# Чат-бот для мероприятий PythonMeetupBot

Telegram чат-бот в котором можно посмотреть расписание докладов мероприятия. А так же задать вопрос докладчику и познакомиться с другими участниками мероприятия.

## Подготовка к запуску
Для запуска сайта вам понадобится Python 3.8+ версии. 

Чтобы скачать код с Github, используйте команду:
```shell
git clone https://github.com/Swatlprus/PythonMeetupBot.git
```
Для создания виртуального окружения используйте команду (Linux):
```shell
python3 -m venv venv
```
Для установки зависимостей, используйте команду:
```shell
pip3 install -r requirements.txt
```

## Настройка переменных окружения
Пример .env файла

``
SECRET_KEY=django-insecure-&%pb8r^9+!lk3rl%is#iz
DEBUG=False
ALLOWED_HOSTS='0.0.0.0.0'
TELEGRAM_TOKEN=65520:AAExux2WuW-GnfEzvAxEgan0g7o
```
SECRET_KEY - Секретный ключ Django, можно сгенерировать
DEBUG - Настройка DEBUG режима. Для "боевого" режима ставим False
ALLOWED_HOSTS - IP адресс или адресс сайта, где будет опубликован проект
TELEGRAM_TOKEN - Токен от Telegram бота. Создать его можно через https://t.me/BotFather

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).