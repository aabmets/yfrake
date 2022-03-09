from yfrake.server import runner
import asyncio


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def test_runner():
    await runner.main()
