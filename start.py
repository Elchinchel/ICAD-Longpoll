# Кто то скажет "спиздил"
# Я скажу "вдохновился"
import sys
import time
import asyncio
import traceback

from requests import post
from requests.exceptions import ConnectionError as ConnErr
from typing import Union

from poller import listen_longpoll
from config import config
from settings import settings
from utils import log


def get_host() -> Union[str, None]:
    host = f"https://{config.username}.pythonanywhere.com"
    r = post(host)
    if r.status_code != 404:
        return host
    host = f"https://{config.username}.eu.pythonanywhere.com"
    r = post(host)
    if r.status_code != 404:
        return host


if config.host is None:
    config.host = get_host()
    if config.host is None:
        print('Не удалось найти сайт\n' +
              'Проверь имя пользователя в config.ini')
        sys.exit()
    log(f'Найден сайт по адресу {config.host}, сохраняю')
    config.sync()

try:
    log(f'Попытка подключения к {config.host}...')
    r = post(config.host+'/longpoll/start', json={"token": config.token})
except ConnErr as e:
    print(f'\n{e.args}\n\nОшибка соединения, проверь host в config.ini и подключение к интернету')  # noqa
    sys.exit()

if r.status_code - 200 > 100:
    print({
        404: 'Не удалось достучаться до сайта',
        500: 'Ошибка на удаленном сервере'
    }.get(r.status_code, 'Сервер вернул неизвестный код'))
    sys.exit()

data: dict = r.json()
if 'error' in data:
    if data['error'] == 0:
        print('Указан неверный токен')
        sys.exit()

config.access_key = data['settings'].pop('key')
config.self_id = data.pop('self_id')
config.sync()

settings.update(data.pop('settings'))

log('Данные получены, запускаю прослушку...')


while True:
    try:
        asyncio.get_event_loop().run_until_complete(
            listen_longpoll(data)
        )
    except Exception:
        log(f'Произошла ошибка!\n{traceback.format_exc()}')
        time.sleep(5)
    except KeyboardInterrupt:
        log('Клавиатурное прерывание, сдыхаю...')
        break
