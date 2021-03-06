# ==================================================================================== #
#    server.py - This file is part of the YFrake package.                              #
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
from ..config.config import ConfigSingleton
from pathlib import Path
import subprocess
import psutil
import sys


# ==================================================================================== #
class ServerSingleton:
    """
    This class contains methods to control
    the YFrake server programmatically.
    """
    # ------------------------------------------------------------------------------------ #
    _err_msg_1 = 'Server is already running! (YFrake)'
    _err_msg_2 = 'Cannot stop server which is not running! (YFrake)'
    _server: subprocess.Popen = None
    _is_running: bool = False
    __instance__ = None

    # Singleton pattern
    # ------------------------------------------------------------------------------------ #
    def __new__(cls):
        if not cls.__instance__:
            cls.__instance__ = super(ServerSingleton, cls).__new__(cls)
        return cls.__instance__

    # ------------------------------------------------------------------------------------ #
    @classmethod
    def is_running(cls) -> bool:
        if isinstance(cls._server, subprocess.Popen):
            return cls._server.poll() is None
        return False

    # ------------------------------------------------------------------------------------ #
    @classmethod
    def start(cls) -> None:
        if cls.is_running():
            raise RuntimeError(cls._err_msg_1)
        config = ConfigSingleton()
        runner_file = get_runner_file_path()
        args = [
            sys.executable, runner_file,
            '--config-file', str(config.file)
        ]
        cls._server = subprocess.Popen(args)

    # ------------------------------------------------------------------------------------ #
    @classmethod
    def stop(cls) -> None:
        if not cls.is_running():
            raise RuntimeError(cls._err_msg_2)
        try:
            parent = psutil.Process(cls._server.pid)
            children = parent.children(recursive=True)
            procs = children + [parent]
            for proc in procs:
                proc.kill()
        except psutil.NoSuchProcess:  # pragma: no cover
            return


# ==================================================================================== #
def get_runner_file_path() -> str:
    runner_file = Path(__file__).with_name('runner.py').resolve()
    return str(runner_file)
