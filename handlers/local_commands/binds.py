import json
from typing import List

from lib.vkmini import VkApi
from utils import send_signal
from settings import settings
from config import config


async def bind_add(args: List[str], payload: str,
                   vk: VkApi, update: list) -> str:
    if not (args and payload):
        return """Использование команды:
        {префикс лп модуля} связать {слово}
        {команда}""".replace('    ', '')
    word = args[0]
    command = payload.splitlines()[0]
    settings.binds.update({word: command})
    await settings.sync()
    return f'✅ Слово "{word}" привязано к команде "{command}"'


async def bind_remove(args: List[str], payload: str,
                      vk: VkApi, update: list) -> str:
    if not args:
        return """Использование команды:
        {префикс лп модуля} отвязать {слово}
        """.replace('    ', '')
    word = args[0]
    if word not in settings.binds:
        return f'⚠️ Слово "{word}" не привязано'
    settings.binds.pop(word)
    await settings.sync()
    return f'✅ Слово "{word}" больше не воспринимается как команда'


async def binds_list(args: List[str], payload: str,
                     vk: VkApi, update: list) -> None:
    await send_signal(json.dumps({
            'access_key': config.access_key,
            'command': 'бинды',
            'message': (await vk('messages.getById',
                                 message_ids=update[1]))['items'][0],
            'chat': None
        },  ensure_ascii=False, separators=(',', ':'))
    )
