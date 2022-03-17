# ==================================================================================== #
#    base_response.py - This file is part of the YFrake package.                       #
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
from .access_controller import AccessController
import copy


# ==================================================================================== #
class BaseResponse:
    """
    Parent class of ClientResponse.
    """
    # ------------------------------------------------------------------------------------ #
    def __init__(self):
        self.permissions = AccessController()
        self._endpoint: str | None = None
        self._error: dict | None = None
        self._data: dict | None = None

    # ------------------------------------------------------------------------------------ #
    @property
    def endpoint(self) -> str | None:
        if not self.permissions.elevated:
            endpoint = getattr(self, '_endpoint', None)
            return copy.deepcopy(endpoint)
        return self._endpoint

    @property
    def error(self) -> dict | None:
        if not self.permissions.elevated:
            error = getattr(self, '_error', None)
            return copy.deepcopy(error)
        return self._error

    @property
    def data(self) -> dict | None:
        if not self.permissions.elevated:
            data = getattr(self, '_data', None)
            return copy.deepcopy(data)
        return self._data

    # ------------------------------------------------------------------------------------ #
    @endpoint.setter
    def endpoint(self, value) -> None:
        if not self.permissions.elevated:
            raise self.permissions.error
        self._endpoint = value

    @error.setter
    def error(self, value) -> None:
        if not self.permissions.elevated:
            raise self.permissions.error
        self._error = value

    @data.setter
    def data(self, value) -> None:
        if not self.permissions.elevated:
            raise self.permissions.error
        self._data = value

    # ------------------------------------------------------------------------------------ #
    @endpoint.deleter
    def endpoint(self) -> None:
        if not self.permissions.elevated:
            raise self.permissions.error
        del self._endpoint

    @error.deleter
    def error(self) -> None:
        if not self.permissions.elevated:
            raise self.permissions.error
        del self._error

    @data.deleter
    def data(self) -> None:
        if not self.permissions.elevated:
            raise self.permissions.error
        del self._data
