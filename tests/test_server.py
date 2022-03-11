from yfrake import server
from urllib import request
import asyncio
import pytest
import json
import time


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def test_server():
    assert server.is_running() is False
    server.start()
    assert server.is_running() is True

    with pytest.raises(RuntimeError):
        server.start()

    url = 'http://localhost:8888/quote_type?symbol=msft'
    with request.urlopen(url=url) as f:
        resp = f.read().decode('utf-8')
    resp = json.loads(resp)

    endpoint = resp.get('endpoint', False)
    error = resp.get('error', False)
    data = resp.get('data', False)

    assert endpoint is not False
    assert error is not False
    assert data is not False

    assert isinstance(endpoint, str)
    assert isinstance(error, type(None))
    assert isinstance(data, dict)

    assert len(data) > 0
    assert data.get('symbol') == 'MSFT'

    assert server.is_running() is True
    server.stop()
    time.sleep(1)
    assert server.is_running() is False

    with pytest.raises(RuntimeError):
        server.stop()
