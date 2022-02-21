# ==================================================================================== #
#    base_worker.py - This file is part of the YFrake package.                         #
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
from .paths import base_url, endpoints
from .response import Response
from .utils import validate
from json import JSONDecodeError
from asyncio import TimeoutError
import aiohttp


# ==================================================================================== #
class BaseWorker:
    """
    Base class which contains the methods required to
    request data from the Yahoo Finance API servers.
    """
    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def _request(params: dict, endpoint: str) -> Response:
        """
        The main function responsible for making the
        requests to the Yahoo Finance API servers.
        """
        url = base_url + endpoints[endpoint]
        if '{symbol}' in url:
            sym = params.pop('symbol', '')
            url = url.format(symbol=sym)
        try:
            error = None
            timeout = aiohttp.ClientTimeout(total=5)
            async with aiohttp.request(
                    method='GET', url=url, params=params,
                    raise_for_status=True, timeout=timeout) as resp:
                data = await resp.json()
                # Yahoo Finance sometimes replies with a successful status code 200 empty response,
                # when the query params are invalid, so we need to ensure that the empty response
                # is being correctly identified and returned to the user as an invalid request.
                if not validate(data):
                    raise aiohttp.ClientResponseError(
                        request_info=resp.request_info,
                        history=resp.history,
                        status=400,
                        message='Bad Request'
                    )
        except aiohttp.ClientResponseError as ex:
            data = None
            error = {
                'type': 'HTTPError',
                'code': ex.status,
                'msg': ex.message,
                'url': url
            }
        except (TimeoutError, JSONDecodeError):
            data = None
            error = {
                'type': 'HTTPError',
                'code': 500,
                'msg': 'Internal server error',
                'url': url
            }
        return Response(
            endpoint=endpoint,
            error=error,
            data=data
        )
