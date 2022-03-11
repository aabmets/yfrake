from yfrake.server import runner
import asyncio
import sys


if sys.platform == 'win32':
    asyncio.set_event_loop_policy(
        asyncio.WindowsSelectorEventLoopPolicy()
    )


async def test_runner():
    await runner.main()
