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
from .thread_loop import ThreadLoop
from .endpoints import Endpoints
from .session import Session
from .validators import validate_and_sanitize
import asyncio
import inspect
import sys


# ==================================================================================== #
class Client:
    _err_msg_1 = 'Configuration decorator already in use! (YFrake)'
    _err_msg_2 = 'Configuration decorator not in use! (YFrake)'
    _err_msg_3 = 'Invalid endpoint \'{0}\'! (YFrake)'
    _err_msg_4 = 'Only a list of dicts can be passed into the \'batch_get\' method! (YFrake)'

    _async_mode: bool = False
    _initialized: bool = False

    # ------------------------------------------------------------------------------------ #
    @classmethod
    def configure(cls, limit: int = 64, timeout: int = 2):
        """
        This decorator opens and closes a session to
        the Yahoo Finance API servers. Other methods
        of the client object can be called only when the
        decorated function or coroutine has not returned.
        """
        if cls._initialized:
            raise RuntimeError(cls._err_msg_1)

        if sys.platform == 'win32':  # pragma: no branch
            policy = asyncio.WindowsSelectorEventLoopPolicy()
            asyncio.set_event_loop_policy(policy)

        def decorator(func):
            async def a_inner(*args, **kwargs):
                await Session.a_open(limit=limit, timeout=timeout)
                await func(*args, **kwargs)
                await Session.a_close()
                cls._initialized = False

            def t_inner(*args, **kwargs):
                Session.t_open(limit=limit, timeout=timeout)
                func(*args, **kwargs)
                Session.t_close()
                cls._initialized = False

            cls._initialized = True
            cls._async_mode = inspect.iscoroutinefunction(func)
            return a_inner if cls._async_mode else t_inner
        return decorator

    # ------------------------------------------------------------------------------------ #
    @classmethod
    def batch_get(cls, queries: list) -> AsyncResults | ThreadResults:
        """
        This method schedules multiple tasks to fetch
        market data from the Yahoo Finance API servers.
        Returns immediately the unfinished results object.
        """
        requests = dict()
        for query in queries:
            if not isinstance(query, dict):
                raise TypeError(cls._err_msg_4)
            resp = cls.get(**query)
            with resp.permissions:
                fut = resp.future
                requests[fut] = resp

        return {
            True: AsyncResults,
            False: ThreadResults
        }[cls._async_mode](requests)

    # ------------------------------------------------------------------------------------ #
    @classmethod
    def get(cls, endpoint: str = '', **kwargs) -> ClientResponse:
        """
        This method schedules a single task to fetch
        market data from the Yahoo Finance API servers.
        Returns immediately the unfinished response object.
        """
        if not cls._initialized:
            raise RuntimeError(cls._err_msg_2)

        attr = 'get_' + endpoint
        func = getattr(Endpoints, attr, None)

        if not func:
            msg = cls._err_msg_3.format(endpoint)
            raise NameError(msg)

        validate_and_sanitize(endpoint, kwargs)
        resp = ClientResponse(cls._async_mode)

        if cls._async_mode:
            future = asyncio.create_task(
                cls._wrapper(endpoint, kwargs, func, resp))
        else:
            future = asyncio.run_coroutine_threadsafe(
                cls._wrapper(endpoint, kwargs, func, resp),
                ThreadLoop.loop)

        with resp.permissions:
            resp.future = future
        return resp

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def _wrapper(cls, endpoint, kwargs, func, resp) -> ClientResponse:
        result = await func(endpoint, **kwargs)
        with resp.permissions:
            resp.endpoint = result['endpoint']
            resp.error = result['error']
            resp.data = result['data']
            resp.event.set()
        return resp
