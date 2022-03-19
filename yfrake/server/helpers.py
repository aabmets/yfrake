# ==================================================================================== #
#    helpers.py - This file is part of the YFrake package.                             #
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
from ..client.paths import paths
from .handler import handler
from .utils import get_default_config
from argparse import ArgumentParser
from argparse import Namespace
from aiohttp_swagger3 import SwaggerFile
from aiohttp_swagger3 import SwaggerUiSettings
from aiohttp import web
import aiohttp_cors as cors


# These functions are called sequentially by the runner.py module.

# ==================================================================================== #
def build_route_table() -> list:
    route_table = list()
    for key in paths.keys():
        path = '/' + key
        route = web.get(path=path, handler=handler)
        route_table.append(route)
    return route_table


# ------------------------------------------------------------------------------------ #
def create_swagger(app, spec) -> SwaggerFile:
    app['storage'] = dict()
    return SwaggerFile(
        app=app,
        spec_file=str(spec),
        swagger_ui_settings=SwaggerUiSettings(path="/")
    )


# ------------------------------------------------------------------------------------ #
def create_cors(app):
    cors_options = cors.ResourceOptions(
        allow_credentials=True,
        expose_headers="*",
        allow_headers="*"
    )
    return cors.setup(
        app=app,
        defaults={'*': cors_options}
    )


# ------------------------------------------------------------------------------------ #
def print_notification(host, port):
    message = f'Running the YFrake server at: http://{host}:{port}'
    print('=' * len(message))
    print(message)
    print('=' * len(message))
    print('\n')


# ------------------------------------------------------------------------------------ #
def get_runtime_args() -> Namespace:  # pragma: no cover
    config = get_default_config()
    parser = ArgumentParser()
    parser.add_argument('--host', type=str, default=config.host)
    parser.add_argument('--port', type=int, default=config.port)
    parser.add_argument('--limit', type=int, default=config.limit)
    parser.add_argument('--timeout', type=int, default=config.timeout)
    parser.add_argument('--backlog', type=int, default=config.backlog)
    return parser.parse_args()
