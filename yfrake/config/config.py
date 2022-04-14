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
from ..cache.cache import CacheSingleton as Cache
from . import helpers, utils
from ..client import session
from pathlib import Path
import copy


# ==================================================================================== #
class ConfigSingleton:
    _err_not_available = 'Operation not available on config object attributes! (YFrake)'
    _err_no_file = 'Config file does not exist at provided path! (YFrake)'
    _err_locked = 'Cannot modify config while session is open! (YFrake)'
    _path = Path()
    _config = dict()
    __instance__ = None

    # Singleton pattern
    # ------------------------------------------------------------------------------------ #
    def __new__(cls):
        if not cls.__instance__:
            cls.__instance__ = super(ConfigSingleton, cls).__new__(cls)
        return cls.__instance__

    # ------------------------------------------------------------------------------------ #
    def __init__(self):
        if not getattr(self, '_config', None):
            self.file = utils.get_default_config_path()
            self.HERE = utils.get_cwd_config_path()

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    def is_locked() -> bool:
        return session.is_locked()

    # ------------------------------------------------------------------------------------ #
    @property
    def file(self) -> Path:
        return self._path

    @file.setter
    def file(self, path: Path | str) -> None:
        if self.is_locked():
            raise RuntimeError(self._err_locked)
        path = Path(path).resolve()
        if not path.exists():
            if path != self.HERE:
                raise RuntimeError(self._err_no_file)
            utils.copy_default_config_to(path)
        self._config = helpers.read_config_from(path)
        Cache.populate_settings(self.settings)
        self._path = path

    @file.deleter
    def file(self) -> None:
        raise TypeError(self._err_not_available)

    # ------------------------------------------------------------------------------------ #
    @property
    def settings(self) -> dict:
        return copy.deepcopy(self._config)

    @settings.setter
    def settings(self, _) -> None:
        raise TypeError(self._err_not_available)

    @settings.deleter
    def settings(self) -> None:
        raise TypeError(self._err_not_available)
