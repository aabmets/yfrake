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
from ..client.endpoints import Endpoints
from ..server.utils import convert_multidict
from aiohttp import web
import json


# ==================================================================================== #
async def handler(request: web.Request) -> web.Response:
    """
    This func handles all incoming requests to the server
    and forwards them to the correct endpoint handlers.
    """
    query = convert_multidict(request.query)  # ensure no double keys
    endpoint = request.path.strip('/')        # get endpoint name from path
    attr = 'get_' + endpoint                  # get endpoint method name
    func = getattr(Endpoints, attr, None)     # get endpoint method
    result = await func(endpoint, **query)    # wait until done
    text = json.dumps(result, indent=3)       # convert dict to str
    return web.Response(text=text)            # return str
