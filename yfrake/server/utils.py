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
from aiohttp.web import Response
from multidict import MultiDictProxy
from pathlib import Path
import configparser
import json


# ==================================================================================== #
def get_server_config() -> dict:
    configfile = Path(__file__).with_name('server.ini')
    config = configparser.ConfigParser()
    config.read(configfile)
    return {
        'host': config['SERVER_DEFAULTS']['host'],
        'port': config['SERVER_DEFAULTS']['port']
    }


# ------------------------------------------------------------------------------------ #
def convert_multidict(multidict: MultiDictProxy) -> dict:
    out = dict()
    for key in multidict.keys():
        if key not in out:
            out[key] = multidict[key]
    return out


# ------------------------------------------------------------------------------------ #
def pretty_json(obj: object) -> Response:
    text = json.dumps(obj=vars(obj), indent=3)
    return Response(text=text)