from .api import VkApi, VkResponseException
from .methods import Messages
from .exceptions import *
from .user_longpoll import LP
from .group_longpoll import LPGroup


import sys
__ver = sys.version_info
if __ver.major < 3 or (__ver.major < 3 and __ver.minor < 6):
    raise OSError('VkMini: Python versions below 3.6 is not supported')
if sys.platform == 'linux':
    import os
    try:
        import uvloop
        import asyncio
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    except ImportError:
        pass