from typing import List
import time

from lib.vkmini import VkApi
from utils import get_plural


pings = {
    'пинг': 'ПОНГ',
    'кинг': 'КИНГ КОНГ ЗА ТОБОЙ! ОБЕРНИСЬ!!!',
    'тик': 'УДАЛИСЬ, ТИКТОКЕР111',
    'пиу': 'ПАУ-ПАУ-ПАУК',
    'ping': 'PONG',
    'биба': 'БОБА',
    'king': 'The Lion King*',
}


async def ping(args: List[str], payload: str, vk: VkApi, update: list) -> str:
    latency = round(time.time() - update[4], 1)
    if latency < 0:
        latency = "(время неправильное, пинга не будет)"
    else:
        latency = f"Задержка ≈{str(latency)} секунд{get_plural(latency, 'а', 'ы', '', 'ы')}"  # noqa
    resp = pings.get(update[7], 'че?')
    return f"{resp} (LP модуль)\n{latency}"
