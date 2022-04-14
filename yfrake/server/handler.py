# ==================================================================================== #
#    handler.py - This file is part of the YFrake package.                             #
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
from .. import client
from ..client.worker import build_error
from ..client.exceptions import BadRequestError
from multidict import MultiDictProxy
from aiohttp import web
import json


# ==================================================================================== #
async def handler(request: web.Request) -> web.Response:
    """
    This func receives all the incoming requests to the server
    and forwards them to the correct endpoint handlers.
    """

    params = convert_multidict(request.query)
    params = convert_datatypes(params)
    endpoint = request.path.strip('/')
    try:
        resp = client.get(endpoint, **params)
        await resp.wait()
        error = resp.error
        data = resp.data

    except (NameError, TypeError, KeyError, BadRequestError):
        error = build_error(BadRequestError)
        data = None

    result = dict(
        endpoint=endpoint,
        error=error,
        data=data
    )
    text = json.dumps(result, indent=3)
    return web.Response(text=text)


# ------------------------------------------------------------------------------------ #
def convert_multidict(multidict: MultiDictProxy) -> dict:
    out = dict()
    for key in multidict.keys():
        if key not in out:
            out[key] = multidict[key]
    return out


# ------------------------------------------------------------------------------------ #
def convert_datatypes(params: dict) -> dict:
    for key, value in params.items():
        try:
            params[key] = int(value)
        except ValueError:
            pass

        if value.lower() == 'true':
            params[key] = True
        if value.lower() == 'false':
            params[key] = False

    return params
