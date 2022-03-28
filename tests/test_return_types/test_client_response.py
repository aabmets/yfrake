from yfrake import client
from concurrent import futures
import threading
import asyncio
import pytest
import sys


if sys.platform == 'win32':
    asyncio.set_event_loop_policy(
        asyncio.WindowsSelectorEventLoopPolicy()
    )


def test_client_response_1():
    @client.session
    def inner():
        resp = client.get(endpoint='quote_type', symbol='msft')
        resp.wait()
        assert isinstance(resp.event, threading.Event)
        assert isinstance(resp.future, futures.Future)
    inner()


async def test_client_response_2():
    @client.session
    async def inner():
        resp = client.get(endpoint='quote_type', symbol='msft')
        await resp.wait()
        assert isinstance(resp.event, asyncio.Event)
        assert isinstance(resp.future, asyncio.Task)
    await inner()


def test_client_response_3():
    @client.session
    def inner():
        resp = client.get(endpoint='quote_type', symbol='msft')
        resp.wait()
        for attr in ['event', 'future']:
            with pytest.raises(TypeError):
                setattr(resp, attr, str())
            with pytest.raises(TypeError):
                delattr(resp, attr)
    inner()
