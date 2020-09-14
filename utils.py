import re

from aiohttp import ClientSession
from typing import Tuple, List, Union

from lib.vkmini import VkApi, VkResponseException, logger
from config import config


printer = logger.Printer()


def log(text):
    printer.info(text)


async def send_signal(data: dict) -> bytes:
    return await async_post(config.host + '/longpoll/event', data)


async def async_post(url: str, data: dict):
    async with ClientSession() as session:
        async with session.post(url, data=data,
                                headers={'content-type': 'application/json'}
                                ) as resp:
            return resp.content


async def async_get(url: str, json: bool = False) -> Union[bytes, dict]:
    async with ClientSession() as session:
        async with session.get(url) as resp:
            if json:
                return resp.json()
            return resp.content


def parse(text: str) -> Tuple[str, List[str], str]:
    matches = re.findall(r'(\S+)|\n(.*)', text)[1:]
    command = matches.pop(0)[0].lower()
    payload = ''
    args = []
    for i, match in enumerate(matches, 1):
        if match[0]:
            args.append(match[0])
        else:
            payload += match[1] + ('\n' if i < len(matches) else '')
    return command, args, payload


def get_plural(number: Union[int, float], one: str, few: str,
               many: str, other: str = '') -> str:
    """`one`  = 1, 21, 31, 41, 51, 61...\n
    `few`  = 2-4, 22-24, 32-34...\n
    `many` = 0, 5-20, 25-30, 35-40...\n
    `other` = 1.31, 2.31, 5.31..."""
    if type(number) == float:
        if not number.is_integer():
            return other
        else:
            number = int(number)
    if number % 10 in {2, 3, 4}:
        return few
    number = str(number)
    if number[-1] == '1':
        return one
    return many


def find_user_mention(text: str) -> Union[int, None]:
    uid = re.findall(r'\[(id|public|club)(\d*)\|', text)
    if uid:
        if uid[0][0] != 'id':
            uid = 0 - int(uid[0][1])
        else:
            uid = int(uid[0][1])
    return uid


async def find_user_by_link(text: str, vk: VkApi) -> Union[int, None]:
    user = re.findall(r"vk.com\/(id\d*|[^ \n]*\b)", text)
    if user:
        try:
            return await (vk('users.get', user_ids=user))[0]['id']
        except (VkResponseException, IndexError):
            return None


async def find_mention_by_message(msg: dict, vk: VkApi) -> Union[int, None]:
    'Возвращает ID пользователя, если он есть в сообщении, иначе None'
    user_id = None
    if msg['text']:
        user_id = find_user_mention(msg['text'])
    if msg.get('reply_message') and not user_id:
        user_id = msg['reply_message']['from_id']
    if not user_id:
        user_id = await find_user_by_link(msg['text'], vk)
    if msg['fwd_messages'] and not user_id:
        user_id = msg['fwd_messages'][0]['from_id']
    return user_id
