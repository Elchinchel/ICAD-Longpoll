import json
from lib.vkmini import VkApi
from utils import send_signal, log
from config import config


async def handle(update: list, vk: VkApi, chats: dict, command: str):
    log(f'Отправляю команду "{command}"...')
    message = (await vk('messages.getById', message_ids=update[1]))['items'][0]
    message['text'] = update[5].replace('<br>', '\n')
    await send_signal(json.dumps({
            'access_key': config.access_key,
            'message': message,
            'chat': chats.get(update[3])
        },  ensure_ascii=False, separators=(',', ':'))
    )
