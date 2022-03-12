from yfrake.client.base_response import BaseResponse
import asyncio
import pytest
import sys


if sys.platform == 'win32':
    asyncio.set_event_loop_policy(
        asyncio.WindowsSelectorEventLoopPolicy()
    )


def test_resp_endpoint():
    resp = BaseResponse()
    assert resp.endpoint is None
    with resp.permissions:
        resp.endpoint = str()
    assert resp.endpoint == str()


def test_resp_endpoint_exceptions():
    resp = BaseResponse()
    with pytest.raises(PermissionError):
        resp.endpoint = str()
    with pytest.raises(RuntimeError):
        del resp.endpoint


def test_resp_error():
    resp = BaseResponse()
    assert resp.error is None
    with resp.permissions:
        resp.error = dict()
    assert resp.error == dict()


def test_resp_error_exceptions():
    resp = BaseResponse()
    with pytest.raises(PermissionError):
        resp.error = dict()
    with pytest.raises(RuntimeError):
        del resp.error


def test_resp_data():
    resp = BaseResponse()
    assert resp.data is None
    with resp.permissions:
        resp.data = dict()
    assert resp.data == dict()


def test_resp_data_exceptions():
    resp = BaseResponse()
    with pytest.raises(PermissionError):
        resp.data = dict()
    with pytest.raises(RuntimeError):
        del resp.data


async def test_response_object():
    resp = BaseResponse()

    assert resp.endpoint is None
    assert resp.error is None
    assert resp.data is None

    async with resp.permissions:
        resp.endpoint = str()
        resp.error = dict()
        resp.data = dict()

    assert resp.endpoint == str()
    assert resp.error == dict()
    assert resp.data == dict()
