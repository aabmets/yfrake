from yfrake import client
from yfrake.client.client_response import ClientResponse
import asyncio
import pytest
import sys


if sys.platform == 'win32':
    asyncio.set_event_loop_policy(
        asyncio.WindowsSelectorEventLoopPolicy()
    )


def test_client_not_configured():
    def inner():
        args = dict()
        with pytest.raises(RuntimeError):
            client.get(**args)
    inner()


def test_client_already_configured():
    @client.configure()
    def inner():
        with pytest.raises(RuntimeError):
            @client.configure()
            def failure():
                pass
    inner()


def test_invalid_endpoint():
    @client.configure()
    def inner():
        args = dict(endpoint='THIS_IS_INVALID', symbol='msft')
        with pytest.raises(NameError):
            client.get(**args)
    inner()


async def test_invalid_param():
    @client.configure()
    async def inner():
        with pytest.raises(KeyError):
            args = dict(endpoint='quote_type', INVALID_KEY=1000)
            client.get(**args)
    await inner()


def test_invalid_datatype():
    @client.configure()
    def inner():
        with pytest.raises(TypeError):
            args = dict(endpoint='quote_type', symbol=1000)
            client.get(**args)
    inner()


def test_invalid_symbol():
    @client.configure()
    def inner():
        args = dict(endpoint='quote_type', symbol='THIS_IS_INVALID')
        resp = client.get(**args)
        resp.wait_for_result()
        assert isinstance(resp, ClientResponse)
        assert bool(resp.endpoint) is True
        assert bool(resp.error) is True
        assert bool(resp.data) is False
    inner()


async def test_async_object():
    @client.configure()
    async def inner():
        args = dict(endpoint='quote_type', symbol='msft')
        resp = client.get(**args)
        while not resp.available():
            await asyncio.sleep(0)
        async_object = resp.get_async_object()
        assert async_object.done()
    await inner()
