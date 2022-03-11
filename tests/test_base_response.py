from yfrake.client.base_response import BaseResponse
import asyncio
import pytest
import sys


if sys.platform == 'win32':
    asyncio.set_event_loop_policy(
        asyncio.WindowsSelectorEventLoopPolicy()
    )


def test_instantiate_with_params():
    resp = BaseResponse(
        endpoint=str(),
        error=list(),
        data=dict()
    )
    assert type(resp.endpoint) is str
    assert type(resp.error) is list
    assert type(resp.data) is dict


def test_instantiate_without_params():
    resp = BaseResponse()
    assert resp.endpoint is None
    assert resp.error is None
    assert resp.data is None


def test_exceptions():
    resp = BaseResponse()

    with pytest.raises(PermissionError):
        resp.endpoint = int()

    with pytest.raises(PermissionError):
        resp.error = int()

    with pytest.raises(PermissionError):
        resp.data = int()

    with pytest.raises(RuntimeError):
        del resp.endpoint

    with pytest.raises(RuntimeError):
        del resp.error

    with pytest.raises(RuntimeError):
        del resp.data


def test_permissions_sync():
    resp = BaseResponse()
    with resp.permissions:

        resp.endpoint = str()
        resp.error = dict()
        resp.data = list()

        assert type(resp.endpoint) is str
        assert type(resp.error) is dict
        assert type(resp.data) is list


async def test_permissions_async():
    resp = BaseResponse()
    async with resp.permissions:
        resp.endpoint = str()
        resp.error = dict()
        resp.data = list()
