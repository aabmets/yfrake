# ==================================================================================== #
#    base_results.py - This file is part of the YFrake package.                        #
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


# ==================================================================================== #
class BaseResults:
    """
    Parent class of AsyncResults and ThreadResults.
    """
    # ------------------------------------------------------------------------------------ #
    def __init__(self, requests: dict):
        self._future_objects = list(requests.keys())
        self._response_objects = list(requests.values())

    # ------------------------------------------------------------------------------------ #
    def __getitem__(self, key) -> ClientResponse:
        return self._response_objects[key]

    def __setitem__(self, key, value) -> None:
        self._response_objects[key] = value

    def __delitem__(self, key) -> None:
        del self._response_objects[key]

    def __len__(self) -> int:
        return len(self._response_objects)

    # ------------------------------------------------------------------------------------ #
    def pending(self) -> bool:
        for resp in self._response_objects:
            if resp.pending():
                return True
        return False

    # ------------------------------------------------------------------------------------ #
    # The 'wait()' function is defined separately in both the AsyncResults and ThreadResults classes, because
    # the 'asyncio.wait()' coroutine returns two sets of tasks, which we don't want to expose to the user.
