from typing import List
import json

from lib.vkmini import VkApi
from utils import send_signal
from settings import settings
from config import config


async def add_prefix(args: List[str], payload: str, *_) -> str:
    prefix = payload.split(' ')
    if prefix == ['']:
        if len(args) == 0:
            return '⚠️ Не указан префикс'
        else:
            prefix = args[0]
    else:
        prefix = prefix[0]
    if prefix in settings.prefixes:
        return '⚠️ Указанный префикс уже существует'
    settings.prefixes.append(prefix)
    await settings.sync()
    return f'✅ Префикс "{prefix}" добавлен'


async def remove_prefix(args: List[str], payload: str, *_) -> str:
    prefix = payload.split(' ')
    if prefix == ['']:
        if len(args) == 0:
            return '⚠️ Не указан префикс'
        else:
            prefix = args[0]
    else:
        prefix = prefix[0]
    if prefix not in settings.prefixes:
        return '⚠️ Указанный префикс не существует'
    if len(settings.prefixes) == 1:
        return '❔ Но тогда не останется ни одного префикса...'
    settings.prefixes.remove(prefix)
    await settings.sync()
    return f'✅ Префикс "{prefix}" удален'


async def prefix_list(args: List[str], payload: str,
                      vk: VkApi, update: list) -> None:
    await send_signal(json.dumps({
            'access_key': config.access_key,
            'command': 'префиксы',
            'message': (await vk('messages.getById',
                                 message_ids=update[1]))['items'][0],
            'chat': None
        },  ensure_ascii=False, separators=(',', ':'))
    )
