# ==================================================================================== #
#    decorator.py - This file is part of the YFrake package.                           #
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
from . import session
import asyncio
import inspect
import sys


class Decorator:
    _err_cfg_missing = 'Configuration decorator not in use! (YFrake)'
    _err_already_cfg = 'Configuration decorator already in use! (YFrake)'
    _err_forgot_to_wait = 'You forgot to (a)wait a response or a results object! (YFrake)'

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
            raise RuntimeError(cls._err_already_cfg)

        if sys.platform == 'win32':  # pragma: no branch
            policy = asyncio.WindowsSelectorEventLoopPolicy()
            asyncio.set_event_loop_policy(policy)

        def decorator(func):
            config = dict(limit=limit, timeout=timeout)

            async def a_inner(*args, **kwargs):
                cls._initialized = True
                await session.open_async(**config)
                await func(*args, **kwargs)
                await session.close_async()
                cls._initialized = False

            def t_inner(*args, **kwargs):
                cls._initialized = True
                session.open_thread(**config)
                func(*args, **kwargs)
                session.close_thread()
                cls._initialized = False

            cls._async_mode = inspect.iscoroutinefunction(func)
            return a_inner if cls._async_mode else t_inner
        return decorator
