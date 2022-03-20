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
from argparse import ArgumentParser
from multidict import MultiDictProxy
from argparse import Namespace
from pathlib import Path
import configparser


# ==================================================================================== #
def get_runner_file_path() -> str:
    runner_file = Path(__file__).with_name('runner.py').resolve()
    return str(runner_file)


# ------------------------------------------------------------------------------------ #
def get_default_config() -> Namespace:
    config_file = Path(__file__).with_name('server.ini').resolve()
    config = configparser.ConfigParser()
    config.read(config_file)
    config = config['DEFAULT_SETTINGS']
    return Namespace(
        host=config['host'],
        port=int(config['port']),
        limit=int(config['limit']),
        timeout=int(config['timeout']),
        backlog=int(config['backlog'])
    )


# ------------------------------------------------------------------------------------ #
def get_runtime_config() -> Namespace:  # pragma: no cover
    config = get_default_config()
    parser = ArgumentParser()
    parser.add_argument('--host', type=str, default=config.host)
    parser.add_argument('--port', type=int, default=config.port)
    parser.add_argument('--limit', type=int, default=config.limit)
    parser.add_argument('--timeout', type=int, default=config.timeout)
    parser.add_argument('--backlog', type=int, default=config.backlog)
    return parser.parse_args()


# ------------------------------------------------------------------------------------ #
def convert_multidict(multidict: MultiDictProxy) -> dict:
    out = dict()
    for key in multidict.keys():
        if key not in out:
            out[key] = multidict[key]
    return out
