from yfrake import client
import asyncio
import sys


if sys.platform == 'win32':
    asyncio.set_event_loop_policy(
        asyncio.WindowsSelectorEventLoopPolicy()
    )


async def test_async_object():
    @client.configure()
    async def inner():
        results = client.get_all(symbol='msft')
        async for resp in results.gather():
            assert bool(resp.error) is False
            assert bool(resp.data) is True
    await inner()
