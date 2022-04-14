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
from yfrake.config.utils import get_runtime_args
from yfrake.server.handler import handler
from yfrake.server import helpers
from yfrake import client, config
from aiohttp import web
import asyncio


# ==================================================================================== #
@client.session
async def server_runner(run_forever=False):
    settings = config.settings['server']
    spec = get_spec_file_path()
    app = web.Application()

    swagger = helpers.create_swagger(app, spec)
    routes = [web.get('/{any}', handler)]
    swagger.add_routes(routes)

    cors = helpers.create_cors(app)
    routes = list(app.router.routes())
    for route in routes:
        cors.add(route)

    runner = web.AppRunner(app=app)
    await runner.setup()

    site = helpers.create_site(runner, settings)
    await site.start()

    helpers.notify_user(settings)
    while run_forever:  # pragma: no cover
        await asyncio.sleep(3600)

    await site.stop()
    await runner.cleanup()


# ------------------------------------------------------------------------------------ #
if __name__ == '__main__':
    args = get_runtime_args()
    config.file = args.get('config_file')
    coro = server_runner(run_forever=True)
    asyncio.run(coro)
