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


def test_guarded_attr_types_sync():
    @client.configure()
    def inner():
        resp = client.get(endpoint='quote_type', symbol='msft')
        resp.wait()

        assert isinstance(resp.event, threading.Event)
        assert isinstance(resp.future, futures.Future)

    inner()


async def test_guarded_attr_types_async():
    @client.configure()
    async def inner():
        resp = client.get(endpoint='quote_type', symbol='msft')
        await resp.wait()

        assert isinstance(resp.event, asyncio.Event)
        assert isinstance(resp.future, asyncio.Task)

    await inner()


def test_guarded_attr_exceptions():
    @client.configure()
    def inner():
        resp = client.get(endpoint='quote_type', symbol='msft')
        resp.wait()

        for attr in ['event', 'future']:
            with pytest.raises(PermissionError):
                setattr(resp, attr, str())
            with pytest.raises(PermissionError):
                delattr(resp, attr)

    inner()


def test_guarded_attr_permissions():
    @client.configure()
    def inner():
        resp = client.get(endpoint='quote_type', symbol='msft')
        resp.wait()

        with resp.permissions:
            for attr in ['event', 'future']:
                setattr(resp, attr, str())
                assert isinstance(getattr(resp, attr), str)
                delattr(resp, attr)
                with pytest.raises(AttributeError):
                    getattr(resp, attr)

    inner()
