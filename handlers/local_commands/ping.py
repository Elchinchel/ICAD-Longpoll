from typing import List
import time

from lib.vkmini import VkApi
from utils import get_plural


pings = {
    'пинг': 'ПОНГ',
    'кинг': 'КОНГ',
    'пиу': 'ПАУ',
    'пинг': 'ПОНГ',
}


async def ping(args: List[str], payload: str, vk: VkApi, update: list) -> str:
    latency = round(time.time() - update[4], 1)
    if latency < 0:
        latency = "(время неправильное, пинга не будет)"
    else:
        latency = f"Задержка ≈{str(latency)} секунд{get_plural(latency, 'а', 'ы', '', 'ы')}"  # noqa
    resp = pings.get(update[5], 'че?')
    return f"{resp} (LP модуль)\n{latency}"
