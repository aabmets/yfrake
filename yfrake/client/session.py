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
from ..config.config import ConfigSingleton
from . import base_url
from threading import Thread
import aiohttp
import asyncio
import time


# ==================================================================================== #
class SessionSingleton:
    """
    This class holds a connection to the Yahoo
    Finance API servers. A session is established
    by the client 'configure' decorator. There can
    only be a single session active at any time.
    """
    # ------------------------------------------------------------------------------------ #
    timeout: aiohttp.ClientTimeout = None
    session: aiohttp.ClientSession = None
    connector: aiohttp.TCPConnector = None
    loop: asyncio.AbstractEventLoop = None
    thread: Thread = None
    locked: bool = False
    __instance__ = None

    # Singleton pattern
    # ------------------------------------------------------------------------------------ #
    def __new__(cls):
        if not cls.__instance__:
            cls.__instance__ = super(SessionSingleton, cls).__new__(cls)
        return cls.__instance__


# ==================================================================================== #
def is_locked() -> bool:
    return SessionSingleton().locked


# ------------------------------------------------------------------------------------ #
def get_event_loop() -> asyncio.AbstractEventLoop:
    return SessionSingleton().loop


# ------------------------------------------------------------------------------------ #
async def open_async() -> None:
    ss = SessionSingleton()
    settings = ConfigSingleton().settings['client']
    ss.timeout = aiohttp.ClientTimeout(total=settings['timeout'])
    ss.connector = aiohttp.TCPConnector(limit=settings['limit'])
    ss.session = aiohttp.ClientSession(
        connector=ss.connector,
        timeout=ss.timeout,
        base_url=base_url,
        raise_for_status=True
    )
    ss.locked = True


# ------------------------------------------------------------------------------------ #
async def close_async() -> None:
    ss = SessionSingleton()
    await ss.session.close()
    ss.locked = False


# ------------------------------------------------------------------------------------ #
def open_thread() -> None:
    ss = SessionSingleton()
    ss.loop = asyncio.new_event_loop()
    ss.thread = Thread(target=run_background_thread, daemon=True)
    ss.thread.start()
    asyncio_run_threadsafe(open_async(), ss.loop)  # blocking


# ------------------------------------------------------------------------------------ #
def close_thread() -> None:
    ss = SessionSingleton()
    asyncio_run_threadsafe(close_async(), ss.loop)  # blocking
    ss.loop.call_soon_threadsafe(ss.loop.stop)

    force_iter = True
    while force_iter or ss.loop.is_running():
        force_iter = False
        time.sleep(0)

    ss.loop.close()
    ss.thread.join()


# ------------------------------------------------------------------------------------ #
def asyncio_run_threadsafe(coro, loop) -> None:
    future = asyncio.run_coroutine_threadsafe(coro, loop)
    future.result()  # blocks until concurrent future is done


# ------------------------------------------------------------------------------------ #
def run_background_thread() -> None:
    ss = SessionSingleton()
    asyncio.set_event_loop(ss.loop)
    ss.loop.run_forever()
