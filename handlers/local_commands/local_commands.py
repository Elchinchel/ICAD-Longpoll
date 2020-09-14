from lib.vkmini import VkApi
from utils import parse
from .ignore import ignore_add, ignore_list, ignore_remove
from .binds import bind_add, binds_list, bind_remove
from .prefixes import add_prefix, remove_prefix
from .ping import pings, ping
from .info import info


commands = {
    '+префикс': add_prefix,
    '-префикс': remove_prefix,
    '+игнор': ignore_add,
    '-игнор': ignore_remove,
    'игнор': ignore_list,
    'игнорлист': ignore_list,
    'связать': bind_add,
    'отвязать': bind_remove,
    'бинды': binds_list,
    'связки': binds_list,
    'инфо': info
}

commands.update({name: ping for name in pings})


async def passer(*any):
    return "Неизвестная команда"


async def handle(update: list, vk: VkApi):
    command, args, payload = parse(update[5])
    update[5] = command
    text = await commands.get(command, passer)(args, payload, vk, update)
    await vk.msg_op(2, update[3], text, update[1])
