# ==================================================================================== #
#    cache.py - This file is part of the YFrake package.                               #
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
from collections import OrderedDict
import asyncio
import hashlib
import pickle


# ==================================================================================== #
class CacheSingleton:
    __cache__ = None
    __instance__ = None

    # Singleton pattern
    # ------------------------------------------------------------------------------------ #
    def __new__(cls):
        if not cls.__instance__:
            cls.__instance__ = super(CacheSingleton, cls).__new__(cls)
        return cls.__instance__

    # ------------------------------------------------------------------------------------ #
    def __init__(self):
        if not self.__cache__:
            self.__cache__ = OrderedDict()
            self._cache_max_size_mb = 0
            self._cache_size_mb = 0

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    def calculate_hex_digest(*args) -> str:
        jar = pickle.dumps(args)
        key = hashlib.sha3_256(jar)
        return key.hexdigest()

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get(cls, endpoint: str, params: dict) -> dict | None:
        digest: str = cls.calculate_hex_digest(endpoint, params)
        jar = await cls.__cache__.get(key=digest, default=None)
        return pickle.loads(jar) if jar else None

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def set(cls, endpoint: str, params: dict, result: dict) -> None:
        digest: str = cls.calculate_hex_digest(endpoint, params)
        jar = pickle.dumps(result)
        ttl = cls.calculate_ttl(endpoint, params)

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def calculate_ttl(endpoint: str, params: dict) -> None:
        pass
