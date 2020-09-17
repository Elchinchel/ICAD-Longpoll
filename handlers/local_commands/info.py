import subprocess
from typing import List

from lib.vkmini import VkApi

VERSION = "0.1.5"


async def info(args: List[str], payload: str,
               vk: VkApi, update: list) -> str:
    subprocess.run("git fetch", shell=True)
    out = subprocess.run("git log origin/master -1 --pretty=format:%B",
                         shell=True, capture_output=True).stdout
    out = out.decode('utf-8').splitlines()
    update_info = 'Доступно обновление! Новая версия: ' + out[0] + '\n'
    if len(out) > 1:
        update_info += 'Что нового:\n' + '\n'.join(out[2:]) + '\n\n'
    if out[0] == VERSION:
        update_info = ''
    return f"{update_info}LP модуль ver. {VERSION}\nБольше инфы в следующих сериях"  # noqa
