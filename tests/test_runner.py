import asyncio
import pytest
import sys

with pytest.warns(RuntimeWarning):
    from yfrake.server import runner


if sys.platform == 'win32':
    asyncio.set_event_loop_policy(
        asyncio.WindowsSelectorEventLoopPolicy()
    )


async def test_runner():
    await runner.main()
