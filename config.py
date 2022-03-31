import os
import sys
import re
from configparser import ConfigParser
from typing import Set


def _get_parser():
    return ConfigParser(allow_no_value=True, delimiters=('=',))


path = os.path.join(os.getcwd(), 'config.ini')

try:
    open(path).close()
except FileNotFoundError:
    with open(path, 'w', encoding='utf-8') as file:
        if os.environ.get("token") and os.environ.get("host"):
            if '.' in os.environ["host"]:
                username, host = '', os.environ["host"]
            else:
                host, username = '', os.environ["host"]
            if len(os.environ["token"]) != 85:
                token = re.search(r'access_token=[a-z0-9]{85}', os.environ["token"])
                if token:
                    os.environ["token"] = token[0][13:]
                else:
                    sys.exit()
            with open(path, 'w', encoding="utf-8") as file:
                file.write(
                    f'[token]\n{os.environ["token"]}\n[username]\n{username}\n[host]\n{host}\n' +
                    f'[access_key]\n[self_id]\n[local_prefixes]\n.лп\n!лп\n/s'
                )
        else:
            print('Окей, давай конфигурнём\n(вставить текст можно выбрав '
                  '"paste" после долгого нажатия на экран)')
            token = input('Введи токен: ')
            if len(token) != 85:
                token = re.search(r'access_token=[a-z0-9]{85}', token)
                if token:
                    token = token[0][13:]
                else:
                    print('Это не токен...')
                    sys.exit()
            username = input('Введи имя пользователя на pythonanywhere ' +
                             '(оставь пустым, если хочешь указать свой хост): ')
            if username == "":
                host = input('Введи адрес дежурного (если протокол не указан, '
                             'буду подключаться через HTTPS): ')
            else:
                host = ""
            with open(path, 'w', encoding="utf-8") as file:
                file.write(
                    f'[token]\n{token}\n[username]\n{username}\n[host]\n{host}\n' +
                    f'[access_key]\n[self_id]\n[local_prefixes]\n.лп\n!лп\n/s'
                )


class Config:
    _raw: dict

    host: str
    token: str
    username: str
    self_id: int
    access_key: str
    local_prefixes: Set[str]

    def __init__(self):
        self._raw = {}
        with open(path, 'r', encoding='utf-8') as file:
            parser = _get_parser()
            parser.read_file(file)
            for name, val in parser.items():
                if len(val) == 0:
                    value = ""
                else:
                    val = [v for v in val.items()]
                    value = val[0][0] if len(val) == 1 else [v[0] for v in val]
                self._raw[name] = value
            self.__dict__.update(self._raw)
            if type(self.local_prefixes) == str:
                self.local_prefixes = [self.local_prefixes]
            self.local_prefixes = set(self.local_prefixes)

    def sync(self):
        parser = _get_parser()
        for key in self._raw:
            if key == 'DEFAULT':
                continue
            parser.add_section(key)
            val = getattr(self, key)
            if type(val) not in {list, set}:
                val = [val]
            for v in val:
                parser.set(key, str(v), None)
        with open(path, 'w', encoding='utf-8') as file:
            parser.write(file)


config = Config()

if config.username == "" and config.host == "":
    print('Необходимо указать имя пользователя или сайт в config.ini')
    sys.exit()
if config.token == "":
    print('Необходимо указать токен в config.ini')
    sys.exit()
if config.host != "":
    if not config.host.startswith('http'):
        config.host = 'https://' + config.host
        config.sync()
