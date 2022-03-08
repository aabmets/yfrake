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
class BaseResponse:
    """
    The base response object of YFrake.
    """
    _error_msg = 'ERROR! The attributes of the response object are read-only!'

    # ------------------------------------------------------------------------------------ #
    def __init__(self, **kwargs):
        self._endpoint: str = kwargs.get('endpoint')
        self._error: dict = kwargs.get('error')
        self._data: dict = kwargs.get('data')

    # ------------------------------------------------------------------------------------ #
    @property
    def endpoint(self) -> str | None:
        return self._endpoint

    @endpoint.setter
    def endpoint(self, _) -> None:
        print(self._error_msg)

    @endpoint.deleter
    def endpoint(self) -> None:
        print(self._error_msg)

    # ------------------------------------------------------------------------------------ #
    @property
    def error(self) -> dict | None:
        return self._error

    @error.setter
    def error(self, _) -> None:
        print(self._error_msg)

    @error.deleter
    def error(self) -> None:
        print(self._error_msg)

    # ------------------------------------------------------------------------------------ #
    @property
    def data(self) -> dict | None:
        return self._data

    @data.setter
    def data(self, _) -> None:
        print(self._error_msg)

    @data.deleter
    def data(self) -> None:
        print(self._error_msg)
