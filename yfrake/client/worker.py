# ==================================================================================== #
#    worker.py - This file is part of the YFrake package.                              #
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
from .validator import validate
from .session import Session
from .paths import paths
from dataclasses import dataclass
import asyncio
import aiohttp
import json


# ==================================================================================== #
@dataclass
class InvalidResponseError(Exception):
    message: str = 'Bad request'
    status: int = 400


# ==================================================================================== #
class Worker(Session):
    @classmethod
    async def request(cls, params: dict, endpoint: str) -> tuple:
        """
        The main function responsible for making the
        requests to the Yahoo Finance API servers.
        """
        url = paths[endpoint]
        if '{symbol}' in url:
            sym = params.pop('symbol', '')
            url = url.format(symbol=sym)
        try:
            error = None
            async with cls.session.get(url=url, params=params) as resp:
                data = await resp.json()
                if not validate(data):
                    raise InvalidResponseError
        except (aiohttp.ClientResponseError, InvalidResponseError,
                asyncio.TimeoutError, json.JSONDecodeError) as ex:
            error = cls._build_error_dict(url, ex)
            data = None
        return data, error

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    def _build_error_dict(url, ex) -> dict:
        default_message = 'Internal server error'
        default_status = 500
        return dict(
            name='HTTPError',
            status=getattr(ex, 'status', default_status),
            message=getattr(ex, 'message', default_message),
            url=url
        )
