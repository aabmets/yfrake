# ==================================================================================== #
#    utils.py - This file is part of the YFrake package.                               #
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
from .paths import base_url, paths
from urllib.parse import urlencode


# ------------------------------------------------------------------------------------ #
def get_path(endpoint: str, params: dict) -> str:
    path = paths[endpoint]
    if '{symbol}' in path:
        sym = params.pop('symbol', '')
        path = path.format(symbol=sym)
    return path


# ------------------------------------------------------------------------------------ #
def build_error(path: str, params: dict, ex=None) -> dict:
    params = '?' + urlencode(params) if params else ''
    default_message = 'Internal server error'
    default_status = 500
    return dict(
        name='HTTPError',
        status=getattr(ex, 'status', default_status),
        message=getattr(ex, 'message', default_message),
        url=base_url + path + params
    )