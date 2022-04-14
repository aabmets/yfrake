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


# ==================================================================================== #
class Decorator:
    _err_sess_already_open = 'Session has already been opened! (YFrake)'
    _async_mode: bool = False

    # ------------------------------------------------------------------------------------ #
    @classmethod
    def session(cls, func):
        """
        This decorator opens and closes a session to
        the Yahoo Finance API servers. Other methods
        of the client object can be called only when the
        decorated function or coroutine has not returned.
        """
        if session.is_locked():
            raise RuntimeError(cls._err_sess_already_open)

        if sys.platform == 'win32':  # pragma: no branch
            policy = asyncio.WindowsSelectorEventLoopPolicy()
            asyncio.set_event_loop_policy(policy)

        async def a_inner(*args, **kwargs) -> None:
            await session.open_async()
            await func(*args, **kwargs)
            await session.close_async()

        def t_inner(*args, **kwargs) -> None:
            session.open_thread()
            func(*args, **kwargs)
            session.close_thread()

        cls._async_mode = inspect.iscoroutinefunction(func)
        return a_inner if cls._async_mode else t_inner
