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
from .utils import build_error, get_path
from .exceptions import BadRequestError
from .session import Session
import asyncio
import aiohttp
import json


# ==================================================================================== #
class Worker(Session):
    @classmethod
    async def request(cls, params: dict, endpoint: str) -> tuple:
        """
        The main function responsible for making the
        requests to the Yahoo Finance API servers.
        """
        path = get_path(endpoint, params)
        error = None
        try:
            async with cls.session.get(url=path, params=params) as resp:
                data = await resp.json()
                if not await validate(data):
                    raise BadRequestError
        except (aiohttp.ClientResponseError, BadRequestError,
                asyncio.TimeoutError, json.JSONDecodeError) as ex:
            error = build_error(path, params, ex)
            data = None
        return data, error
