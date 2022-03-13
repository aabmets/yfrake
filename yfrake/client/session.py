# ==================================================================================== #
#    session.py - This file is part of the YFrake package.                             #
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
from .thread_loop import ThreadLoop
from .paths import base_url
import aiohttp
import asyncio


# ==================================================================================== #
class Session:
    """
    This class holds a connection to the Yahoo
    Finance API servers. A session is established
    by the client 'configure' decorator. There can
    only be a single session active at any time.
    """
    timeout: aiohttp.ClientTimeout | None = None
    session: aiohttp.ClientSession | None = None
    connector: aiohttp.TCPConnector | None = None

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def a_open(cls, limit, timeout) -> None:
        cls.timeout = aiohttp.ClientTimeout(total=timeout)
        cls.connector = aiohttp.TCPConnector(limit=limit)
        cls.session = aiohttp.ClientSession(
            connector=cls.connector,
            timeout=cls.timeout,
            base_url=base_url,
            raise_for_status=True
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def a_close(cls) -> None:
        await cls.session.close()

    # ------------------------------------------------------------------------------------ #
    @classmethod
    def t_open(cls, limit, timeout) -> None:
        coro = cls.a_open(limit=limit, timeout=timeout)
        ThreadLoop.start_thread_loop()
        cls.schedule(coro)

    # ------------------------------------------------------------------------------------ #
    @classmethod
    def t_close(cls) -> None:
        coro = cls.a_close()
        cls.schedule(coro)
        ThreadLoop.stop_thread_loop()

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    def schedule(coro) -> None:
        future = asyncio.run_coroutine_threadsafe(coro, ThreadLoop.loop)
        future.result()  # concurrent future blocks until coro is done
