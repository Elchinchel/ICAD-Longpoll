import json
from typing import List

from lib.vkmini import VkApi
from utils import send_signal
from settings import settings
from config import config


async def bind_add(args: List[str], payload: str, *_) -> str:
    if not (args and payload):
        return """Использование команды:
        {префикс лп модуля} связать {слово}
        {команда}""".replace('    ', '')
    word = args[0]
    cmd_words = payload.split(' ')
    if not (cmd_words[0] in settings.prefixes or cmd_words[0] in config.local_prefixes):  # noqa
        payload = settings.prefixes[0] + ' ' + payload
    else:
        cmd_words[0] = cmd_words[1]
    settings.binds.update({word.lower(): payload})
    await settings.sync()
    return f'✅ Слово "{word}" привязано к команде "{cmd_words[0]}"'


async def bind_remove(args: List[str], *_) -> str:
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
