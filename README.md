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

```
SECRET_KEY=django-insecure-&%pb8r^9+!lk3rl%is#iz
DEBUG=False
ALLOWED_HOSTS='0.0.0.0.0'
TG_TOKEN=65520:AAExux2WuW-GnfEzvAxEgan0g7o
USDT_ADDRESS=432tesfssfeqqef
BTC_ADDRESS=31ne1zr1zZfh7ju6D9QQozqKfFmYDWqGVn.
VISA_MASTERCARD=1234 5678 9012 3244
```

SECRET_KEY - Секретный ключ Django, можно сгенерировать
DEBUG - Настройка DEBUG режима. Для "боевого" режима ставим False
ALLOWED_HOSTS - IP адресс или адресс сайта, где будет опубликован проект
TG_TOKEN - Токен от Telegram бота. Создать его можно через https://t.me/BotFather
USDT_ADDRESS - Адрес кошелька валюты USDT
BTC_ADDRESS - Адрес кошелька валюты DTC
VISA_MASTERCARD - Номер карты Visa или MasterCard

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).