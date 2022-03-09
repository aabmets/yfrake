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
from asyncio import Task
import threading
import asyncio


# ==================================================================================== #
class ClientResponse(BaseResponse):
    """
    The return type of 'client.get'.
    """
    def __init__(self, async_object: Task | Future):
        async_object.add_done_callback(self._callback)
        obj_type = type(async_object)
        module = {
            Task: asyncio,
            Future: threading
        }[obj_type]
        self._event = module.Event()
        self._async_object = async_object
        super().__init__()

    # ------------------------------------------------------------------------------------ #
    def _callback(self, obj: Task | Future):
        resp: BaseResponse = obj.result()
        with resp.permissions:
            self._endpoint = resp.endpoint
            self._error = resp.error
            self._data = resp.data
        self._event.set()

    # ------------------------------------------------------------------------------------ #
    def get_async_object(self) -> Task | Future | None:
        return self._async_object

    # ------------------------------------------------------------------------------------ #
    def available(self) -> bool:
        return self._event.is_set()

    # ------------------------------------------------------------------------------------ #
    def wait_for_result(self) -> None:
        self._event.wait()

    # ------------------------------------------------------------------------------------ #
    async def result(self) -> None:
        await self._event.wait()
