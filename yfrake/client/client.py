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
from .client_response import ClientResponse
from .thread_loop import ThreadLoop
from .endpoints import Endpoints
from .session import Session
from .validators import validate_and_sanitize
import asyncio
import inspect
import sys


# ==================================================================================== #
class Client:
    _err_msg_1 = 'Invalid endpoint \'{0}\'! (YFrake)'
    _err_msg_2 = 'Configuration decorator not in use! (YFrake)'
    _err_msg_3 = 'Configuration decorator already in use! (YFrake)'

    _async_mode: bool | None = None

    # ------------------------------------------------------------------------------------ #
    @classmethod
    def get(cls, endpoint: str = '', **kwargs) -> ClientResponse:
        """
        This method is used to fetch market data
        from the Yahoo Finance API servers.
        Works in sync and async modes both.
        """
        if cls._async_mode is None:
            raise RuntimeError(cls._err_msg_2)

        attr = 'get_' + endpoint
        if func := getattr(Endpoints, attr, None):
            validate_and_sanitize(endpoint, kwargs)
            if cls._async_mode is True:
                async_object = asyncio.create_task(
                    func(endpoint, **kwargs))
            else:
                async_object = asyncio.run_coroutine_threadsafe(
                    func(endpoint, **kwargs), ThreadLoop.loop)
            return ClientResponse(async_object)

        msg = cls._err_msg_1.format(endpoint)
        raise NameError(msg)

    # ------------------------------------------------------------------------------------ #
    @classmethod
    def configure(cls, limit: int = 60, timeout: int = 2):
        """
        This decorator opens and closes a session to Yahoo Finance API servers.
        It must be used once before any calls to the client 'get' method
        are made inside the decorated function.
        """
        if cls._async_mode is not None:
            raise RuntimeError(cls._err_msg_3)

        if sys.platform == 'win32':  # pragma: no branch
            policy = asyncio.WindowsSelectorEventLoopPolicy()
            asyncio.set_event_loop_policy(policy)

        def decorator(func):
            async def a_inner(*args, **kwargs):
                await Session.a_open(limit=limit, timeout=timeout)
                await func(*args, **kwargs)
                await Session.a_close()
                cls._async_mode = None

            def t_inner(*args, **kwargs):
                Session.t_open(limit=limit, timeout=timeout)
                func(*args, **kwargs)
                Session.t_close()
                cls._async_mode = None

            cls._async_mode = inspect.iscoroutinefunction(func)
            return a_inner if cls._async_mode else t_inner
        return decorator
