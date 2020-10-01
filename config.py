import os
import sys
from lib.isthisapigeon import parse, make
from typing import Set

path = os.path.join(os.getcwd(), 'config.ini')

try:
    with open(path, 'r'):
        pass
except FileNotFoundError:
    with open(path, 'w', encoding='utf-8') as file:
        file.write(
            "[token]\n# Токен нужно вставить ПОД эту строку, 85 символов\n\n"
            "[username]\n# Сюда нужно вставить имя пользователя на pythonanywhere\n\n"  # noqa
            "[host]\n# Если не указано поле \"username\", сюда нужно вставить ссылку на callback модуль\n\n"  # noqa
            "# Поля ниже заполнять не нужно\n[access_key]\n[self_id]\n"
            "[local_prefixes]\n/s\n!лп\n.лп"
        )
        print('Создан конфигурационный файл config.ini, необходимо заполнить')
        sys.exit()


class Config:
    _raw: dict

    host: str
    token: str
    username: str
    self_id: int
    access_key: str
    local_prefixes: Set[str]

    def __init__(self):
        with open(path, 'r', encoding='utf-8') as cfg:
            self._raw, self.__format = parse(cfg.read(), save_format=True)
            self.__dict__.update(self._raw)
            self.local_prefixes = set(self.local_prefixes)
            if self.username is None:
                self.username = ""

    def sync(self):
        for key in self._raw:
            self._raw[key] = getattr(self, key)
        with open(path, 'w', encoding='utf-8') as cfg:
            cfg.write(make(self._raw, self.__format))


config = Config()

if config.username == "" and config.host is None:
    print('Необходимо указать имя пользователя или сайт в config.ini')
    sys.exit()
if config.token is None:
    print('Необходимо указать токен в config.ini')
    sys.exit()
if config.host is not None:
    if not config.host.startswith('http'):
        config.host = 'https://' + config.host
        config.sync()
