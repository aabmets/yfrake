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
from .return_types.client_response import ClientResponse
from .return_types.async_results import AsyncResults
from .return_types.thread_results import ThreadResults
from .get_all_queries import GetAllQueries
from .decorator import Decorator
from .thread_loop import ThreadLoop
from .endpoints import Endpoints
from .validators import validate_and_sanitize
import asyncio
import uuid


# ==================================================================================== #
class Client(Decorator):
    _err_invalid_ep = 'Invalid endpoint \'{0}\'! (YFrake)'
    _err_bad_type = 'Only a list of dicts can be passed into the \'batch_get\' method! (YFrake)'

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def _wrapper(cls, endpoint, kwargs, func, resp) -> ClientResponse:
        _uuid = uuid.uuid4()
        cls._requests[_uuid] = resp  # doesn't need a lock
        result = await func(endpoint, **kwargs)

        setattr(resp, '_endpoint', result['endpoint'])
        setattr(resp, '_error', result['error'])
        setattr(resp, '_data', result['data'])
        getattr(resp, '_event').set()

        cls._requests.pop(_uuid)  # doesn't need a lock
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
        cls.raise_if_not_configured()

        attr = 'get_' + endpoint
        if func := getattr(Endpoints, attr, None):
            validate_and_sanitize(endpoint, kwargs)
            resp = ClientResponse(cls._async_mode)
            if cls._async_mode:
                future = asyncio.create_task(
                    cls._wrapper(endpoint, kwargs, func, resp))
            else:
                future = asyncio.run_coroutine_threadsafe(
                    cls._wrapper(endpoint, kwargs, func, resp),
                    ThreadLoop.loop)
            setattr(resp, '_future', future)
            return resp

        msg = cls._err_invalid_ep.format(endpoint)
        raise NameError(msg)

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
            if not isinstance(query, dict):
                raise TypeError(cls._err_bad_type)
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
        This helper method obtains all the available data about
        the provided symbol from the Yahoo Finance API servers.
        Returns immediately with either the pending
        AsyncResults or ThreadResults collection.
        """
        queries = GetAllQueries(symbol)
        return cls.batch_get(queries)
