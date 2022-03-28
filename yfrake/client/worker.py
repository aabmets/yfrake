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
from .validators import validate_response
from .exceptions import BadRequestError
from .session import SessionSingleton
from . import paths
from aiohttp import ClientError


# ==================================================================================== #
async def request(endpoint: str, kwargs: dict) -> tuple:
    """
    The main function responsible for making the
    web requests to the Yahoo Finance API servers.
    """
    path = get_path(endpoint, kwargs)
    sanitize_booleans_to_strings(kwargs)
    try:
        ss = SessionSingleton()
        async with ss.session.get(url=path, params=kwargs) as resp:
            data = await resp.json()
            await validate_response(data)
            error = None
    except (ClientError, BadRequestError) as ex:
        error = build_error(ex)
        data = None
    return data, error


# ------------------------------------------------------------------------------------ #
def get_path(endpoint: str, params: dict) -> str:
    path = paths.get(endpoint)
    if '{symbol}' in path:
        sym = params.pop('symbol', '')
        path = path.format(symbol=sym)
    return path


# ------------------------------------------------------------------------------------ #
def sanitize_booleans_to_strings(params: dict) -> None:
    for key, value in params.items():
        if isinstance(value, bool):
            params[key] = str(value).lower()


# ------------------------------------------------------------------------------------ #
def build_error(ex=None) -> dict:
    default_message = 'Internal server error'
    default_status = 500
    return dict(
        name='HTTPError',
        status=getattr(ex, 'status', default_status),
        message=getattr(ex, 'message', default_message)
    )
