# я хз че там по ограничениям запросов на PA
# возможно стоит хранить настройки локально?
import os
import json

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
        settings._raw = data
        settings.__dict__.update(data)
        settings.binds_keys = set(settings.binds.keys())

    async def sync(self):
        await async_post(config.host+'/longpoll/sync', json.dumps({
                'access_key': config.access_key,
                'settings': self._raw
            }, ensure_ascii=False))
        self.binds_keys = set(self.binds.keys())


settings = Settings()
