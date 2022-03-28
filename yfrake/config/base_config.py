# ==================================================================================== #
#    base_config.py - This file is part of the YFrake package.                         #
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
class BaseConfig:
    _err_msg = 'Operation not available on config object attributes! (YFrake)'
    _config: dict = None

    # ------------------------------------------------------------------------------------ #
    @property
    def limit(self) -> int:
        return self._config['client']['limit']

    @limit.setter
    def limit(self, _) -> None:
        raise TypeError(self._err_msg)

    @limit.deleter
    def limit(self) -> None:
        raise TypeError(self._err_msg)

    # ------------------------------------------------------------------------------------ #
    @property
    def timeout(self) -> int:
        return self._config['client']['timeout']

    @timeout.setter
    def timeout(self, _) -> None:
        raise TypeError(self._err_msg)

    @timeout.deleter
    def timeout(self) -> None:
        raise TypeError(self._err_msg)

    # ------------------------------------------------------------------------------------ #
    @property
    def host(self) -> str:
        return self._config['server']['host']

    @host.setter
    def host(self, _) -> None:
        raise TypeError(self._err_msg)

    @host.deleter
    def host(self) -> None:
        raise TypeError(self._err_msg)

    # ------------------------------------------------------------------------------------ #
    @property
    def port(self) -> int:
        return self._config['server']['port']

    @port.setter
    def port(self, _) -> None:
        raise TypeError(self._err_msg)

    @port.deleter
    def port(self) -> None:
        raise TypeError(self._err_msg)

    # ------------------------------------------------------------------------------------ #
    @property
    def backlog(self) -> int:
        return self._config['server']['backlog']

    @backlog.setter
    def backlog(self, _) -> None:
        raise TypeError(self._err_msg)

    @backlog.deleter
    def backlog(self) -> None:
        raise TypeError(self._err_msg)

    # ------------------------------------------------------------------------------------ #
    @property
    def cache_size_mb(self) -> int:
        return self._config['other']['cache_size_mb']

    @cache_size_mb.setter
    def cache_size_mb(self, _) -> None:
        raise TypeError(self._err_msg)

    @cache_size_mb.deleter
    def cache_size_mb(self) -> None:
        raise TypeError(self._err_msg)

    # ------------------------------------------------------------------------------------ #
    @property
    def cache_ttl(self) -> dict:
        return dict(self._config['cache_ttl'])

    @cache_ttl.setter
    def cache_ttl(self, _) -> None:
        raise TypeError(self._err_msg)

    @cache_ttl.deleter
    def cache_ttl(self) -> None:
        raise TypeError(self._err_msg)
