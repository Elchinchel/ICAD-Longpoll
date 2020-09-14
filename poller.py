import asyncio

from lib.vkmini import VkApi, LP, logger
from handlers import remote_commands
from handlers.local_commands import local_commands
from utils import log
from config import config
from settings import settings


vk: VkApi

start_deleting = asyncio.Event()
delete_ids = []


async def deleter():
    global delete_ids
    while True:
        await start_deleting.wait()
        start_deleting.clear()
        _delete_ids = delete_ids
        delete_ids = []
        await vk('messages.delete', message_ids=','.join(_delete_ids))


def delete(msg_ids: list):
    delete_ids.extend([str(i) for i in msg_ids])
    start_deleting.set()


async def listen_longpoll(user_data: dict):  # noqa
    global vk
    vk = VkApi(config.token, excepts=True)
    loop = asyncio.get_event_loop()
    lp = await LP.create_poller(vk)
    chats = {user_data['chats'][c]['peer_id']: c for c in user_data['chats']}
    log('Запущено!')
    async for update in lp.listen():
        if update[0] != 4:
            continue
        if update[2] & 2 != 2:
            if update[3] > 2e9:
                if update[6].get('from', 0) in settings.ignored_users:
                    delete([update[1]])
            else:
                if str(update[3]) in settings.ignored_users:
                    delete([update[1]])
        else:
            words = update[5].replace('<br>', ' ').split(' ', 2)
            if words[0] in settings.binds_keys:
                words = [settings.prefixes[0], settings.binds[words[0]].split(' ')] + words[2:]  # noqa
            if len(words) < 2:
                continue
            if words[0] in settings.prefixes:
                loop.create_task(
                    remote_commands.handle(update, vk, chats, words[1])
                )
            if words[0] in config.local_prefixes:
                loop.create_task(
                    local_commands.handle(update, vk)
                )
