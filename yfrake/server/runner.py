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
from yfrake.server.utils import get_runtime_config
from yfrake.server.utils import get_default_config
from yfrake.server.handler import handler
from yfrake.server import helpers
from yfrake import client
from aiohttp import web
import warnings
import asyncio


# ==================================================================================== #
if __name__ != '__main__':  # pragma: no branch
    message = "\n" \
        "╔═══════════════════════════════════════════════════╗\n" \
        "║ The 'runner.py' file is not meant to be imported! ║\n" \
        "║ Use 'from yfrake import server' instead! (YFrake) ║\n" \
        "╚═══════════════════════════════════════════════════╝\n"
    warnings.warn(message, category=RuntimeWarning, stacklevel=100)


# ------------------------------------------------------------------------------------ #
@client.configure()
async def main(run_forever=False):
    spec = get_spec_file_path()
    app = web.Application()
    config = {
        True: get_runtime_config,
        False: get_default_config
    }[run_forever]()

    swagger = helpers.create_swagger(app, spec)
    routes = [web.get('/{any}', handler)]
    swagger.add_routes(routes)

    cors = helpers.create_cors(app)
    routes = list(app.router.routes())
    for route in routes:
        cors.add(route)

    runner = web.AppRunner(app=app)
    await runner.setup()

    site = web.TCPSite(
        runner=runner,
        host=config.host,
        port=config.port,
        backlog=config.backlog)
    await site.start()

    helpers.print_notification(config.host, config.port)
    while run_forever:  # pragma: no cover
        await asyncio.sleep(3600)

    await site.stop()
    await runner.cleanup()


# ------------------------------------------------------------------------------------ #
if __name__ == '__main__':
    coro = main(run_forever=True)
    asyncio.run(coro)
