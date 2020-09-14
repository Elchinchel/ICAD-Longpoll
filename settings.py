# я хз че там по ограничениям запросов на PA
# вdозсожно стоит хранить настройки локально?
import os
from requests import post
from config import config
from typing import List, Set
from utils import async_post

path = os.path.join(os.getcwd(), 'config.ini')


class Settings:
    _raw: dict

    binds: dict
    binds_keys: Set[str]
    ignored_users: List[str]
    prefixes: List[str]

    def __init__(self, data: dict = None):
        pass

    @staticmethod
    def update(data: dict):
        global settings
        settings.__dict__.update(data)
        settings.binds_keys = set(settings.binds.keys())

    async def sync(self):
        for key in self._raw:
            self._raw[key] = getattr(self, key)
        async_post(config.host+'/longpoll/sync', {
                'access_key': config.access_key,
                'settings': self._raw
            })
        self.binds_keys = set(self.binds.keys())


settings = Settings()
