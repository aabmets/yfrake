from yfrake.client.client_response import ClientResponse
from yfrake import client
import asyncio
import pytest


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


test_cases = [
    dict(
        endpoint='historical_prices',
        symbol='qwerty123456',
        interval='1h',
        startDate=1609502400,
        endDate=1612180800,
        events=False,
        extHours=True
    ),
    dict(
        endpoint='historical_prices',
        symbol='qwerty123456',
        interval='1wk',
        range='1y',
        events=True,
        extHours=False
    ),
    dict(
        endpoint='options',
        symbol='qwerty123456',
        startDate=1609502400,
        endDate=1612180800,
        straddle=True,
        getAllData=False,
    ),
    dict(
        endpoint='options',
        symbol='qwerty123456',
        startDate=1609502400,
        endDate=1612180800,
        straddle=False,
        getAllData=True,
    ),
    dict(
        endpoint='shares_outstanding',
        symbol='qwerty123456',
        startDate=1609502400,
        endDate=1612180800
    ),
    dict(endpoint='insights', symbol='qwerty123456'),
    dict(endpoint='quotes_overview', symbols='qwerty123456'),
    dict(endpoint='esg_chart', symbol='qwerty123456'),
    dict(endpoint='quote_type', symbol='qwerty123456'),
    dict(endpoint='recommendations', symbol='qwerty123456'),
    dict(endpoint='esg_scores', symbol='qwerty123456'),
    dict(endpoint='purchase_activity', symbol='qwerty123456'),
    dict(endpoint='earnings', symbol='qwerty123456'),
    dict(endpoint='price_overview', symbol='qwerty123456'),
    dict(endpoint='calendar_events', symbol='qwerty123456'),
    dict(endpoint='company_overview', symbol='qwerty123456'),
    dict(endpoint='sec_filings', symbol='qwerty123456'),
    dict(endpoint='detailed_summary', symbol='qwerty123456'),
    dict(endpoint='financials', symbol='qwerty123456'),
    dict(endpoint='recommendation_trend', symbol='qwerty123456'),
    dict(endpoint='ratings_history', symbol='qwerty123456'),
    dict(endpoint='earnings_history', symbol='qwerty123456'),
    dict(endpoint='earnings_trend', symbol='qwerty123456'),
    dict(endpoint='key_stats', symbol='qwerty123456'),
    dict(endpoint='income_statements', symbol='qwerty123456'),
    dict(endpoint='cashflow_statements', symbol='qwerty123456'),
    dict(endpoint='balance_statements', symbol='qwerty123456'),
    dict(endpoint='institution_ownership', symbol='qwerty123456'),
    dict(endpoint='fund_ownership', symbol='qwerty123456'),
    dict(endpoint='major_holders', symbol='qwerty123456'),
    dict(endpoint='insider_transactions', symbol='qwerty123456'),
    dict(endpoint='insider_holders', symbol='qwerty123456')
]


@pytest.mark.parametrize('args', test_cases)
async def test_client_async(args):
    @client.configure()
    async def inner():
        resp = client.get(**args)
        await resp.result()
        assert isinstance(resp, ClientResponse)
        assert bool(resp.endpoint) is True
        assert bool(resp.error) is True
        assert bool(resp.data) is False
    await inner()
