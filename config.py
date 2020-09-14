import os
import sys
from lib.isthisapigeon import parse, make
from typing import Set

path = os.path.join(os.getcwd(), 'config.ini')


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

    def sync(self):
        for key in self._raw:
            self._raw[key] = getattr(self, key)
        with open(path, 'w', encoding='utf-8') as cfg:
            cfg.write(make(self._raw, self.__format))


config = Config()

if config.username is None and config.host is None:
    print('Необходимо указать имя пользователя или сайт в config.ini')
    sys.exit()
if config.token is None:
    print('Необходимо указать токен в config.ini')
    sys.exit()
if not config.host.startswith('http'):
    config.host = 'http://' + config.host
    config.sync()
