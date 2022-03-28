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
from . import utils
from .base_config import BaseConfig
from .validator import validate_config
from configparser import ConfigParser
from pathlib import Path


# ==================================================================================== #
class ConfigSingleton(BaseConfig):
    HERE = utils.get_cwd_config_path()
    _err_no_file = 'Config file does not exist at provided path! (YFrake)'
    _err_locked = 'Cannot modify config while session is open! (YFrake)'
    _locked = False
    __instance__ = None

    # Singleton pattern
    # ------------------------------------------------------------------------------------ #
    def __new__(cls):
        if not cls.__instance__:
            cls.__instance__ = super(ConfigSingleton, cls).__new__(cls)
            cls.__init_once__(cls.__instance__)
        return cls.__instance__

    # ------------------------------------------------------------------------------------ #
    def __init_once__(self):
        default = utils.get_default_config_path()
        self._read_config_from(default)
        self._locked = False

    # ------------------------------------------------------------------------------------ #
    def _raise_if_unable(self, path: Path) -> None:
        if not path.exists():
            raise RuntimeError(self._err_no_file)
        if self._locked:
            raise RuntimeError(self._err_locked)

    # ------------------------------------------------------------------------------------ #
    def _read_config_from(self, path: Path) -> None:
        if path == self.HERE and not path.exists():
            utils.copy_default_config_to(path)
        self._raise_if_unable(path)
        cp = ConfigParser()
        cp.read(path)
        config = utils.convert_to_dict(cp)
        validate_config(config)
        self._config = config
        self._path = path

    # ------------------------------------------------------------------------------------ #
    def is_locked(self) -> bool:
        return self._locked


# ==================================================================================== #
def toggle_config_lock() -> None:
    config = ConfigSingleton()
    locked = getattr(config, '_locked')
    setattr(config, '_locked', not locked)
