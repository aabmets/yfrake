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
from yfrake.openapi.utils import get_spec_file_path
from yfrake.server.utils import get_default_config
from yfrake.server.helpers import build_route_table
from yfrake.server.helpers import get_runtime_args
from yfrake.server.helpers import create_swagger
from yfrake.server.helpers import create_cors
from yfrake.server.helpers import print_notification
from yfrake.client.session import Session
from aiohttp import web
import asyncio
import sys


# This module runs the YFrake server.

# ==================================================================================== #
async def main(config=None, run_forever=False):
    config = config if config else get_default_config()

    app = web.Application()
    spec = get_spec_file_path()
    routes = build_route_table()

    swagger = create_swagger(app, spec)
    swagger.add_routes(routes)

    cors = create_cors(app)
    routes = list(app.router.routes())
    for route in routes:
        cors.add(route)

    await Session.a_open(
        limit=config.limit,
        timeout=config.timeout
    )
    runner = web.AppRunner(app=app)
    await runner.setup()

    site = web.TCPSite(
        runner=runner,
        host=config.host,
        port=config.port,
        backlog=config.backlog
    )
    await site.start()

    print_notification(config.host, config.port)

    while run_forever:  # pragma: no cover
        await asyncio.sleep(3600)

    await site.stop()
    await runner.cleanup()
    await Session.a_close()


# ------------------------------------------------------------------------------------ #
if __name__ == '__main__':
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(
            asyncio.WindowsSelectorEventLoopPolicy()
        )
    args = dict(
        config=get_runtime_args(),
        run_forever=True
    )
    asyncio.run(
        main(**args)
    )
