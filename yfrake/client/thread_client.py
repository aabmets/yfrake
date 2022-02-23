# ==================================================================================== #
#    thread_client.py - This file is part of the YFrake package.                       #
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
from .async_client import AsyncClient
from threading import Thread, Lock
import asyncio
import copy


# ==================================================================================== #
class ThreadClient:
    """
    Instances of this class enable the user
    to make requests to the Yahoo Finance API
    from a synchronous (procedural) context.
    """
    _error_msg = 'ERROR! The response attribute of the ThreadClient object is read-only!'
    _thread, _loop = None, None
    _class_lock = Lock()

    # ------------------------------------------------------------------------------------ #
    @classmethod
    def _start_background_loop(cls) -> None:
        asyncio.set_event_loop(cls._loop)
        cls._loop.run_forever()

    # ------------------------------------------------------------------------------------ #
    @classmethod
    def _resurrect_thread_loop(cls) -> None:
        cls._loop = asyncio.new_event_loop()
        cls._thread = Thread(
            target=cls._start_background_loop, daemon=True)
        cls._thread.start()

    # ------------------------------------------------------------------------------------ #
    @classmethod
    def _is_thread_loop_alive(cls) -> bool:
        alive = True
        if (not isinstance(cls._loop, asyncio.AbstractEventLoop)
                or cls._loop.is_closed()):
            alive = False
        if (not isinstance(cls._thread, Thread)
                or not cls._thread.is_alive()):
            alive = False
        return alive

    # ------------------------------------------------------------------------------------ #
    def __init__(self):
        if self._class_lock.acquire(blocking=False):
            if not self._is_thread_loop_alive():
                self._resurrect_thread_loop()
            self._class_lock.release()
        self._response = None
        self._future = None

    # ------------------------------------------------------------------------------------ #
    def is_busy(self) -> bool:
        if self._future:
            return not self._future.done()
        return False

    # ------------------------------------------------------------------------------------ #
    def is_done(self) -> bool:
        if self._future:
            return self._future.done()
        return True

    # ------------------------------------------------------------------------------------ #
    def get(self, endpoint: str, **kwargs) -> None:
        if self.is_done():
            if func := getattr(AsyncClient, 'get_' + endpoint, None):
                self._future = asyncio.run_coroutine_threadsafe(
                    func(**kwargs), self._loop)
                self._future.add_done_callback(
                    self._set_response)

    # ------------------------------------------------------------------------------------ #
    def _set_response(self, future) -> None:
        self._response = future.result()

    # ------------------------------------------------------------------------------------ #
    @property
    def response(self):
        if self.is_done():
            return copy.deepcopy(self._response)
        return None

    @response.setter
    def response(self, _):
        print(self._error_msg)

    @response.deleter
    def response(self):
        print(self._error_msg)
