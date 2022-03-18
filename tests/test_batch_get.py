from yfrake.client.return_types.client_response import ClientResponse
from yfrake import client
import asyncio
import pytest
import sys
import time


if sys.platform == 'win32':
    asyncio.set_event_loop_policy(
        asyncio.WindowsSelectorEventLoopPolicy()
    )

queries = [
    dict(endpoint='quote_type', symbol='msft'),
    dict(endpoint='price_overview', symbol='aapl'),
    dict(endpoint='key_statistics', symbol='tsla')
]


def test_batch_get_1():
    @client.configure()
    def inner():
        results = client.batch_get(queries)
        results.wait()
        for resp in results:
            assert bool(resp.error) is False
            assert bool(resp.data) is True
    inner()


def test_batch_get_2():
    @client.configure()
    def inner():
        results = client.batch_get(queries)
        while results.pending():
            time.sleep(0.001)
        for resp in results:
            assert bool(resp.error) is False
            assert bool(resp.data) is True
    inner()


def test_batch_get_3():
    @client.configure()
    def inner():
        results = client.batch_get(queries)
        for resp in results.gather():
            assert bool(resp.error) is False
            assert bool(resp.data) is True
    inner()


def test_batch_get_4():
    @client.configure()
    def inner():
        results = client.batch_get(queries)
        for resp in results.as_completed():
            assert bool(resp.error) is False
            assert bool(resp.data) is True
    inner()


async def test_batch_get_5():
    @client.configure()
    async def inner():
        results = client.batch_get(queries)
        await results.wait()
        for resp in results:
            assert bool(resp.error) is False
            assert bool(resp.data) is True
    await inner()


async def test_batch_get_6():
    @client.configure()
    async def inner():
        results = client.batch_get(queries)
        while results.pending():
            await asyncio.sleep(0.001)
        for resp in results:
            assert bool(resp.error) is False
            assert bool(resp.data) is True
    await inner()


async def test_batch_get_7():
    @client.configure()
    async def inner():
        results = client.batch_get(queries)
        async for resp in results.gather():
            assert bool(resp.error) is False
            assert bool(resp.data) is True
    await inner()


async def test_batch_get_8():
    @client.configure()
    async def inner():
        results = client.batch_get(queries)
        async for resp in results.as_completed():
            assert bool(resp.error) is False
            assert bool(resp.data) is True
    await inner()


async def test_batch_get_9():
    @client.configure()
    async def inner():
        results = client.batch_get(queries)
        await results.wait()

        assert len(results) == len(queries)
        assert isinstance(results[0], ClientResponse)
        results[0] = str()
        assert isinstance(results[0], str)
        del results[0]
        assert len(results) < len(queries)
    await inner()


async def test_batch_get_10():
    @client.configure()
    async def inner():
        _queries = ['asdfg']
        with pytest.raises(TypeError):
            client.batch_get(_queries)
    await inner()
