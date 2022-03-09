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
import asyncio
import inspect
import sys


# ==================================================================================== #
class Client:
    async_mode: bool | None = None

    @classmethod
    def get(cls, endpoint: str = '', **kwargs) -> ClientResponse:
        func = getattr(Endpoints, 'get_' + endpoint, None)
        if cls.async_mode is None:
            raise RuntimeError('YFrake is not configured!')
        elif func is None:
            raise AttributeError('Invalid YFrake endpoint!')
        else:
            if cls.async_mode:
                async_object = asyncio.create_task(func(**kwargs))
            else:
                async_object = asyncio.run_coroutine_threadsafe(
                    func(**kwargs), ThreadLoop.loop)
            return ClientResponse(async_object)

    # ------------------------------------------------------------------------------------ #
    @classmethod
    def configure(cls, limit: int = 60, timeout: int = 2):
        if sys.platform == 'win32':
            policy = asyncio.WindowsSelectorEventLoopPolicy()
            asyncio.set_event_loop_policy(policy)

        def decorator(func):
            async def a_inner(*args, **kwargs):
                await Session.a_open(limit=limit, timeout=timeout)
                await func(*args, **kwargs)
                await Session.a_close()

            def t_inner(*args, **kwargs):
                Session.t_open(limit=limit, timeout=timeout)
                func(*args, **kwargs)
                Session.t_close()

            cls.async_mode = inspect.iscoroutinefunction(func)
            return a_inner if cls.async_mode else t_inner
        return decorator
