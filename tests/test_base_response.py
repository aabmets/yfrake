from yfrake.client.return_types.base_response import BaseResponse
import asyncio
import pytest
import sys


if sys.platform == 'win32':
    asyncio.set_event_loop_policy(
        asyncio.WindowsSelectorEventLoopPolicy()
    )


def test_resp_attributes():
    resp = BaseResponse()
    assert resp.endpoint is None
    assert resp.error is None
    assert resp.data is None


def test_resp_endpoint_exceptions():
    resp = BaseResponse()
    with pytest.raises(RuntimeError):
        resp.endpoint = str()
    with pytest.raises(RuntimeError):
        del resp.endpoint


def test_resp_error_exceptions():
    resp = BaseResponse()
    with pytest.raises(RuntimeError):
        resp.error = dict()
    with pytest.raises(RuntimeError):
        del resp.error


def test_resp_data_exceptions():
    resp = BaseResponse()
    with pytest.raises(RuntimeError):
        resp.data = dict()
    with pytest.raises(RuntimeError):
        del resp.data
