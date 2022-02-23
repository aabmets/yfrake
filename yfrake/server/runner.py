# ==================================================================================== #
#    runner.py - This file is part of the YFrake package.                              #
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
from yfrake.server.handlers import Handlers
from yfrake.server.utils import get_server_config
from yfrake.openapi.utils import get_spec_file_path
from aiohttp_swagger3 import SwaggerFile, SwaggerUiSettings
from aiohttp import web
from argparse import ArgumentParser
import inspect


# ==================================================================================== #
def main():
    config = get_server_config()
    parser = ArgumentParser()
    parser.add_argument('--host', type=str, default=config['host'])
    parser.add_argument('--port', type=int, default=config['port'])
    args = parser.parse_args()

    routes = list()
    route_table: list = inspect.getmembers(
        Handlers, predicate=inspect.isfunction)
    for name, func in route_table:
        if name.startswith('handler_'):
            path = '/'.join(name.split('handler_'))
            routes.append(web.get(path=path, handler=func))

    app = web.Application()
    swagger = SwaggerFile(
        app=app,
        spec_file=str(get_spec_file_path()),
        swagger_ui_settings=SwaggerUiSettings(path="/")
    )
    swagger.add_routes(routes)
    app['storage'] = dict()
    web.run_app(
        app=app,
        host=args.host,
        port=args.port
    )


# ------------------------------------------------------------------------------------ #
if __name__ == '__main__':
    main()
