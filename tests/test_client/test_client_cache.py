from yfrake.cache.cache import CacheSingleton
from yfrake import client
from datetime import datetime
import asyncio
import sys


if sys.platform == 'win32':
    asyncio.set_event_loop_policy(
        asyncio.WindowsSelectorEventLoopPolicy()
    )


async def test_client_cache():
    cache = CacheSingleton()
    while len(cache.cache) != 0:
        cache.cache.popitem()

    @client.session
    async def inner():
        args = dict(endpoint='quote_type', symbol='msft')
        start_1 = datetime.now()
        resp_1 = client.get(**args)
        await resp_1.wait()
        end_1 = datetime.now()
        diff_1 = end_1 - start_1

        start_2 = datetime.now()
        resp_2 = client.get(**args)
        await resp_2.wait()
        end_2 = datetime.now()
        diff_2 = end_2 - start_2

        assert resp_1.data == resp_2.data
        assert diff_1 > diff_2

    await inner()
