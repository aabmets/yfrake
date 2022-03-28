# ==================================================================================== #
#    config.py - This file is part of the YFrake package.                              #
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
from .base_config import BaseConfig
from .validator import validate_config
from .utils import read_config_file
from .utils import get_default_config_path
from .utils import get_cwd_config_path
from pathlib import Path


# ==================================================================================== #
class ConfigSingleton(BaseConfig):
    HERE = get_cwd_config_path()
    _path: Path = None
    __instance__ = None

    # Singleton pattern
    # ------------------------------------------------------------------------------------ #
    def __new__(cls):
        if not cls.__instance__:
            cls.__instance__ = super(ConfigSingleton, cls).__new__(cls)
        return cls.__instance__

    # ------------------------------------------------------------------------------------ #
    def __init__(self) -> None:
        if not self.file:
            self.file = get_default_config_path()

    # ------------------------------------------------------------------------------------ #
    def __iter__(self):
        for key in self._config.keys():
            yield key

    # ------------------------------------------------------------------------------------ #
    def __getitem__(self, key) -> dict:
        return dict(self._config[key])  # break reference

    def __setitem__(self, key, value) -> None:
        raise TypeError(self._err_msg)

    def __delitem__(self, key) -> None:
        raise TypeError(self._err_msg)

    # ------------------------------------------------------------------------------------ #
    @property
    def file(self) -> Path:
        return self._path

    @file.setter
    def file(self, path: Path) -> None:
        config = read_config_file(path)
        validate_config(config)
        self._config = config
        self._path = path

    @file.deleter
    def file(self) -> None:
        raise TypeError(self._err_msg)
