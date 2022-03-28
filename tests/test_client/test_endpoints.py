from tests.test_client.queries.good_queries import good_queries
from tests.test_client.queries.bad_queries import bad_queries
from yfrake import client
import asyncio
import pytest
import sys


if sys.platform == 'win32':
    asyncio.set_event_loop_policy(
        asyncio.WindowsSelectorEventLoopPolicy()
    )


test_queries = good_queries + bad_queries


@pytest.mark.parametrize('args', test_queries)
async def test_client_async(args):
    @client.session
    async def inner():
        query = args.get('query')
        endpoint = query.get('endpoint')

        resp = client.get(**query)
        await resp.wait()

        assert resp.endpoint == endpoint
        assert bool(resp.error) is args.get('expected_error')
        assert bool(resp.data) is args.get('expected_data')
    await inner()
