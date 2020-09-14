# import re
from typing import List

from lib.vkmini import VkApi
# from utils import async_get

VERSION = "0.1.0"


async def info(args: List[str], payload: str,
               vk: VkApi, update: list) -> str:
    # data = await async_get(
    #     'raw.githubusercontent.com/elchinchel/icad_lp/master' +
    #     '/handlers/local_commands/info.py'
    # )
    # last_v = re.findall(r'VERSION = "(.+?)"', str(data))[0][0]
    # if last_v != VERSION:  # бля похуй потом сделаю
    return "Здесь будет инфа, но сейчас ее не будет"
