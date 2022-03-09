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
import copy


# ==================================================================================== #
class AccessController:
    def __init__(self):
        self.elevated = False

    def __enter__(self):
        self.elevated = True

    def __exit__(self, t, v, b):
        self.elevated = False

    async def __aenter__(self):
        self.elevated = True

    async def __aexit__(self, t, v, b):
        self.elevated = False


# ==================================================================================== #
class BaseResponse:
    """
    The base response object of YFrake.
    """
    _err_msg_1 = 'Insufficient permissions to modify response object attributes!'
    _err_msg_2 = 'It is illegal to delete response object attributes!'

    # ------------------------------------------------------------------------------------ #
    def __init__(self, **kwargs):
        self.permissions = AccessController()
        self._endpoint: str = kwargs.get('endpoint')
        self._error: dict = kwargs.get('error')
        self._data: dict = kwargs.get('data')

    # ------------------------------------------------------------------------------------ #
    @property
    def endpoint(self) -> str | None:
        if not self.permissions.elevated:
            return copy.deepcopy(self._endpoint)
        return self._endpoint

    @property
    def error(self) -> dict | None:
        if not self.permissions.elevated:
            return copy.deepcopy(self._error)
        return self._error

    @property
    def data(self) -> dict | None:
        if not self.permissions.elevated:
            return copy.deepcopy(self._data)
        return self._data

    # ------------------------------------------------------------------------------------ #
    @endpoint.setter
    def endpoint(self, value) -> None:
        if not self.permissions.elevated:
            raise PermissionError(self._err_msg_1)
        self._endpoint = value

    @error.setter
    def error(self, value) -> None:
        if not self.permissions.elevated:
            raise PermissionError(self._err_msg_1)
        self._error = value

    @data.setter
    def data(self, value) -> None:
        if not self.permissions.elevated:
            raise PermissionError(self._err_msg_1)
        self._data = value

    # ------------------------------------------------------------------------------------ #
    @endpoint.deleter
    def endpoint(self) -> None:
        raise RuntimeError(self._err_msg_2)

    @error.deleter
    def error(self) -> None:
        raise RuntimeError(self._err_msg_2)

    @data.deleter
    def data(self) -> None:
        raise RuntimeError(self._err_msg_2)
