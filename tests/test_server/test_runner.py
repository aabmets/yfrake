from yfrake.server.runner import server_runner
import asyncio
import sys


if sys.platform == 'win32':
    asyncio.set_event_loop_policy(
        asyncio.WindowsSelectorEventLoopPolicy()
    )


async def test_runner():
    await server_runner()
