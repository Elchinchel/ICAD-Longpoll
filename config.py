import yaml
import os
import sys
import re
from configparser import ConfigParser
from typing import Set


def _get_parser():
    return ConfigParser(allow_no_value=True, delimiters=('=',))


path = os.path.join(os.getcwd(), 'config.yaml')

try:
    with open(path, 'r') as x:
        if x.read() == '':
            x.close()
            raise FileNotFoundError
except FileNotFoundError:
    with open(path, 'w', encoding='utf-8') as file:
        if os.environ.get("token") and os.environ.get("host"):
            if '.' in os.environ["host"]:
                username, host = '', os.environ["host"]
            else:
                host, username = '', os.environ["host"]
            if os.environ["token"].startswith('vk1.a.'):
                token = os.environ["token"]
            else:
                token = re.search(r'access_token=[^&]+', os.environ["token"])
                if token:
                    os.environ["token"] = token[0][13:]
                else:
                    print("No access token found")
                    sys.exit()
            
            with open(path, 'w', encoding="utf-8") as file:
                file.write(yaml.dump({"token": token, "host": host, "username": username, "access_key": '', "self_id": '',
                           "local_prefixes": ['.лп', '!лп', '/s']}))
                """file.write(
                    f'[token]\n{os.environ["token"]}\n[username]\n{username}\n[host]\n{host}\n' +
                    f'[access_key]\n[self_id]\n[local_prefixes]\n.лп\n!лп\n/s'
                )"""
        else:
            print('Окей, давай конфигурнём\n(вставить текст можно выбрав '
                  '"paste" после долгого нажатия на экран)')
            token = input('Введи токен: ')
            if not token.startswith('vk1.a.'):
                token = re.search(r'access_token=[^&]+', token)
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
                    yaml.dump({"token": token, "host": host, "username": username, "access_key": '', "self_id": '',
                               "local_prefixes": ['.лп', '!лп', '/s']}))


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

            parser = yaml.safe_load(file.read())
            print(parser)
            """parser = _get_parser()
            parser.read_file(file)"""
            for name, val in parser.items():
                print(name, val)
                if len(val) == 0:
                    value = ""
                else:
                    value = val
                self._raw[name] = value
            self.__dict__.update(self._raw)
            if type(self.local_prefixes) == str:
                self.local_prefixes = [self.local_prefixes]
            self.local_prefixes = set(self.local_prefixes)
            print(self._raw)

    def sync(self):
        with open(path, 'w', encoding='utf-8') as file:
            file.write(yaml.dump(self._raw))


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
