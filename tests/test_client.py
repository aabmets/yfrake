from yfrake.client.client_response import ClientResponse
from yfrake import client
import asyncio
import pytest


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


valid_test_cases = [
    dict(
        endpoint='historical_prices',
        symbol='msft',
        interval='1h',
        startDate=1609502400,
        endDate=1612180800,
        events=False,
        extHours=True
    ),
    dict(
        endpoint='historical_prices',
        symbol='msft',
        interval='1wk',
        range='1y',
        events=True,
        extHours=False
    ),
    dict(
        endpoint='options',
        symbol='msft',
        startDate=1609502400,
        endDate=1612180800,
        straddle=True,
        getAllData=False,
    ),
    dict(
        endpoint='options',
        symbol='msft',
        startDate=1609502400,
        endDate=1612180800,
        straddle=False,
        getAllData=True,
    ),
    dict(
        endpoint='shares_outstanding',
        symbol='msft',
        startDate=1609502400,
        endDate=1612180800
    ),
    dict(endpoint='insights', symbol='msft'),
    dict(endpoint='quotes_overview', symbols='msft,aapl,tsla'),
    dict(endpoint='esg_chart', symbol='msft'),
    dict(endpoint='quote_type', symbol='msft'),
    dict(endpoint='news', symbol='msft'),
    dict(endpoint='recommendations', symbol='msft'),
    dict(endpoint='validate_symbols', symbols='msft,aapl,tsla'),
    dict(endpoint='market_summary'),
    dict(endpoint='trending_symbols'),
    dict(endpoint='currencies'),
    dict(endpoint='esg_scores', symbol='msft'),
    dict(endpoint='purchase_activity', symbol='msft'),
    dict(endpoint='earnings', symbol='msft'),
    dict(endpoint='price_overview', symbol='msft'),
    dict(endpoint='calendar_events', symbol='msft'),
    dict(endpoint='company_overview', symbol='msft'),
    dict(endpoint='sec_filings', symbol='msft'),
    dict(endpoint='detailed_summary', symbol='msft'),
    dict(endpoint='financials', symbol='msft'),
    dict(endpoint='recommendation_trend', symbol='msft'),
    dict(endpoint='ratings_history', symbol='msft'),
    dict(endpoint='earnings_history', symbol='msft'),
    dict(endpoint='earnings_trend', symbol='msft'),
    dict(endpoint='key_stats', symbol='msft'),
    dict(endpoint='income_statements', symbol='msft'),
    dict(endpoint='cashflow_statements', symbol='msft'),
    dict(endpoint='balance_statements', symbol='msft'),
    dict(endpoint='institution_ownership', symbol='msft'),
    dict(endpoint='fund_ownership', symbol='msft'),
    dict(endpoint='major_holders', symbol='msft'),
    dict(endpoint='insider_transactions', symbol='msft'),
    dict(endpoint='insider_holders', symbol='msft')
]


def test_client_not_configured():
    def inner():
        args = dict()
        with pytest.raises(RuntimeError):
            client.get(**args)
    inner()


def test_invalid_endpoint():
    @client.configure()
    def inner():
        args = dict(endpoint='THIS_IS_INVALID', symbol='msft')
        with pytest.raises(AttributeError):
            client.get(**args)
    inner()


def test_invalid_symbol():
    @client.configure()
    def inner():
        args = dict(endpoint='quote_type', symbol='THIS_IS_INVALID')
        resp = client.get(**args)
        resp.wait_for_result()
        assert bool(resp.endpoint) is True
        assert bool(resp.error) is True
        assert bool(resp.data) is False
    inner()


async def test_while_not_available():
    @client.configure()
    async def inner():
        args = dict(endpoint='quote_type', symbol='msft')
        resp = client.get(**args)
        while not resp.available():
            await asyncio.sleep(0)
        async_object = resp.get_async_object()
        assert async_object.done()
    await inner()


@pytest.mark.parametrize('args', valid_test_cases)
async def test_client_async(args):
    @client.configure()
    async def inner():
        resp = client.get(**args)
        await resp.result()
        assert isinstance(resp, ClientResponse)
        assert bool(resp.endpoint) is True
        assert bool(resp.error) is False
        assert bool(resp.data) is True
    await inner()
