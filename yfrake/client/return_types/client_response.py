# ==================================================================================== #
#    client_response.py - This file is part of the YFrake package.                     #
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
from .base_response import BaseResponse
from concurrent.futures import Future
from typing import Coroutine
from asyncio import Task
import threading
import asyncio


# ==================================================================================== #
class ClientResponse(BaseResponse):
    """
    Datatype returned by the client 'get' method.
    """
    def __init__(self, async_mode: bool):
        self._future: Task | Future | None = None
        self._event = {
            True: asyncio.Event,
            False: threading.Event
        }[async_mode]()
        super().__init__()

    # ------------------------------------------------------------------------------------ #
    def pending(self) -> bool:
        return not self._event.is_set()

    # ------------------------------------------------------------------------------------ #
    def wait(self) -> Coroutine | None:
        if isinstance(self._event, asyncio.Event):
            return self._event.wait()  # return a coro
        self._event.wait()  # block until event is set

    # ------------------------------------------------------------------------------------ #
    @property
    def event(self) -> asyncio.Event | threading.Event:
        return self._event

    @event.setter
    def event(self, _) -> None:
        self._raise_error()

    @event.deleter
    def event(self) -> None:
        self._raise_error()

    # ------------------------------------------------------------------------------------ #
    @property
    def future(self) -> Task | Future | None:
        return self._future

    @future.setter
    def future(self, _) -> None:
        self._raise_error()

    @future.deleter
    def future(self) -> None:
        self._raise_error()
