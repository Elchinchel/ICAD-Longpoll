import json
from lib.vkmini import VkApi
from utils import send_signal, log
from config import config


async def handle(update: list, vk: VkApi, chats: dict, command: str):
    log(f'Отправляю команду "{command}"...')
    await send_signal(json.dumps({
            'access_key': config.access_key,
            'command': command,
            'message': (await vk('messages.getById',
                                 message_ids=update[1]))['items'][0],
            'chat': chats.get(update[3])
        },  ensure_ascii=False, separators=(',', ':'))
    )
