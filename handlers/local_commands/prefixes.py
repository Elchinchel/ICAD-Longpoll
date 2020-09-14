from typing import List

from lib.vkmini import VkApi
from settings import settings


async def add_prefix(args: List[str], payload: str, vk: VkApi, u) -> str:
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


async def remove_prefix(args: List[str], payload: str, vk: VkApi, u) -> str:
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
    settings.prefixes.remove(prefix)
    await settings.sync()
    return f'✅ Префикс "{prefix}" удален'
