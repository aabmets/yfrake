# ==================================================================================== #
#    client.py - This file is part of the YFrake package.                              #
# ------------------------------------------------------------------------------------ #
#                                                                                      #
#    MIT License                                                                       #
#                                                                                      #
#    Copyright (c) 2022 Mattias Aabmets                                                #
#                                                                                      #
#    Permission is hereby granted, free of charge, to any person obtaining a copy      #
#    of this software and associated documentation files (the "Software"), to deal     #
#    in the Software without restriction, including without limitation the rights      #
#    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell         #
#    copies of the Software, and to permit persons to whom the Software is             #
#    furnished to do so, subject to the following conditions:                          #
#                                                                                      #
#    The above copyright notice and this permission notice shall be included in all    #
#    copies or substantial portions of the Software.                                   #
#                                                                                      #
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR        #
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,          #
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE       #
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER            #
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,     #
#    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE     #
#    SOFTWARE.                                                                         #
#                                                                                      #
# ==================================================================================== #
from ..cache.cache import CacheSingleton
from .return_types import ClientResponse
from .return_types import AsyncResults
from .return_types import ThreadResults
from .validators import validate_request
from .decorator import Decorator
from . import endpoints
from . import session
import asyncio


# ==================================================================================== #
class ClientSingleton(Decorator):
    _err_sess_not_open = 'Session has not been opened! (YFrake)'
    _cache = CacheSingleton()
    __instance__ = None

    # Singleton pattern
    # ------------------------------------------------------------------------------------ #
    def __new__(cls):
        if not cls.__instance__:
            cls.__instance__ = super(ClientSingleton, cls).__new__(cls)
        return cls.__instance__

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def _wrapper(cls, endpoint: str, params: dict, resp: ClientResponse) -> ClientResponse:
        result = cls._cache.get(endpoint, params)
        if not result:
            attr = 'get_' + endpoint
            func = getattr(endpoints, attr)
            result = await func(endpoint, dict(params))
            cls._cache.set(endpoint, params, result)
        setattr(resp, '_endpoint', result['endpoint'])
        setattr(resp, '_error', result['error'])
        setattr(resp, '_data', result['data'])
        getattr(resp, '_event').set()
        return resp

    # ------------------------------------------------------------------------------------ #
    @classmethod
    def get(cls, endpoint: str = '', **kwargs) -> ClientResponse:
        """
        This method schedules a single task to fetch
        market data from the Yahoo Finance API servers.
        Returns immediately with the pending
        ClientResponse object.
        """
        if not session.is_locked():
            raise RuntimeError(cls._err_sess_not_open)

        validate_request(endpoint, kwargs)
        resp = ClientResponse(cls._async_mode)

        if cls._async_mode:
            future = asyncio.create_task(
                cls._wrapper(endpoint, kwargs, resp))
        else:
            loop = session.get_event_loop()
            future = asyncio.run_coroutine_threadsafe(
                cls._wrapper(endpoint, kwargs, resp), loop)

        setattr(resp, '_future', future)
        return resp

    # ------------------------------------------------------------------------------------ #
    @classmethod
    def batch_get(cls, queries: list) -> AsyncResults | ThreadResults:
        """
        This helper method schedules multiple tasks to fetch
        market data from the Yahoo Finance API servers.
        Returns immediately with either the pending
        AsyncResults or ThreadResults collection.
        """
        requests = dict()
        for query in queries:
            resp = cls.get(**query)
            fut = resp.future
            requests[fut] = resp

        return {
            True: AsyncResults,
            False: ThreadResults
        }[cls._async_mode](requests)

    # ------------------------------------------------------------------------------------ #
    @classmethod
    def get_all(cls, symbol: str) -> AsyncResults | ThreadResults:
        """
        This helper method obtains all the available data about a symbol.
        Returns immediately with either the pending
        AsyncResults or ThreadResults collection.
        """
        queries = [
            dict(endpoint='historical_prices', symbol=symbol, interval='1d', range='max', events=True, extHours=True),
            dict(endpoint='shares_outstanding', symbol=symbol, startDate=946728000, endDate=3162293065),
            dict(endpoint='options', symbol=symbol, getAllData=True),
            dict(endpoint='balance_statements', symbol=symbol),
            dict(endpoint='calendar_events', symbol=symbol),
            dict(endpoint='cashflow_statements', symbol=symbol),
            dict(endpoint='company_overview', symbol=symbol),
            dict(endpoint='detailed_summary', symbol=symbol),
            dict(endpoint='earnings', symbol=symbol),
            dict(endpoint='earnings_history', symbol=symbol),
            dict(endpoint='earnings_trend', symbol=symbol),
            dict(endpoint='esg_chart', symbol=symbol),
            dict(endpoint='esg_scores', symbol=symbol),
            dict(endpoint='financials', symbol=symbol),
            dict(endpoint='fund_ownership', symbol=symbol),
            dict(endpoint='income_statements', symbol=symbol),
            dict(endpoint='insider_holders', symbol=symbol),
            dict(endpoint='insider_transactions', symbol=symbol),
            dict(endpoint='insights', symbol=symbol),
            dict(endpoint='institution_ownership', symbol=symbol),
            dict(endpoint='key_statistics', symbol=symbol),
            dict(endpoint='major_holders', symbol=symbol),
            dict(endpoint='news', symbol=symbol),
            dict(endpoint='price_overview', symbol=symbol),
            dict(endpoint='purchase_activity', symbol=symbol),
            dict(endpoint='quote_type', symbol=symbol),
            dict(endpoint='quotes_overview', symbols=symbol),
            dict(endpoint='ratings_history', symbol=symbol),
            dict(endpoint='recommendation_trend', symbol=symbol),
            dict(endpoint='recommendations', symbol=symbol),
            dict(endpoint='sec_filings', symbol=symbol),
            dict(endpoint='validate_symbols', symbols=symbol)
        ]
        return cls.batch_get(queries)
