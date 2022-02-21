# ==================================================================================== #
#    sync_client.py - This file is part of the YFrake package.                         #
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
from .response import Response
from threading import Thread
import asyncio
import copy


# ==================================================================================== #
class SyncClient:
    """
    Instances of this class enable the user
    to make requests to the Yahoo Finance API
    from a synchronous (procedural) context.
    """
    error_msg = 'ERROR! The response attribute of the SyncClient object is read-only!'

    # ------------------------------------------------------------------------------------ #
    def __init__(self):
        self._response: Response = Response()
        self._loop = asyncio.new_event_loop()
        self._thread = Thread(target=self._start_background_loop, daemon=True)
        self._thread.start()
        self._future = None

    # ------------------------------------------------------------------------------------ #
    def _start_background_loop(self) -> None:
        asyncio.set_event_loop(self._loop)
        self._loop.run_forever()

    # ------------------------------------------------------------------------------------ #
    def _set_response(self, future) -> None:
        self._response = future.result()

    # ------------------------------------------------------------------------------------ #
    def request(self, endpoint: str, **kwargs) -> None:
        if self.is_done():
            if func := getattr(AsyncClient, 'get_' + endpoint, None):
                self._future = asyncio.run_coroutine_threadsafe(func(**kwargs), self._loop)
                self._future.add_done_callback(self._set_response)

    # ------------------------------------------------------------------------------------ #
    def is_busy(self) -> bool:
        if self._future is not None:
            return not self._future.done()
        return False

    # ------------------------------------------------------------------------------------ #
    def is_done(self) -> bool:
        if self._future is not None:
            return self._future.done()
        return True

    # ------------------------------------------------------------------------------------ #
    @property
    def response(self):
        if self.is_done():
            return copy.deepcopy(self._response)
        return None

    @response.setter
    def response(self, _):
        print(self.error_msg)

    @response.deleter
    def response(self):
        print(self.error_msg)
