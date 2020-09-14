from typing import Union
from aiohttp import ClientSession
from .exceptions import NetworkError


async def post(url: str, data: Union[dict, str, bytes],
               excepts: bool = False, **kwargs) -> dict:
    async with ClientSession() as session:
        async with session.post(url, data=data, **kwargs) as resp:
            if resp.status == 200:
                return await resp.json()
            elif excepts:
                raise NetworkError(resp.status)


async def longpoll_get(url: str, excepts: bool = False) -> dict:
    async with ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                return await resp.json()
            else:
                if excepts:
                    raise NetworkError(resp.status)
                return {}
