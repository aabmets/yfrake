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
from . import utils
from collections import OrderedDict
import json


# ==================================================================================== #
class CacheSingleton:
    max_entry_size: int
    max_entries: int
    max_memory: int

    ttl_groups: dict
    ttl_short: dict
    ttl_long: dict

    mem_in_use = 0
    cache = OrderedDict()
    __instance__ = None

    # Singleton pattern
    # ------------------------------------------------------------------------------------ #
    def __new__(cls):
        if not cls.__instance__:
            cls.__instance__ = super(CacheSingleton, cls).__new__(cls)
        return cls.__instance__

    # ------------------------------------------------------------------------------------ #
    @classmethod
    def populate_settings(cls, config: dict) -> None:
        cls.max_entries = config['cache_size']['max_entries']
        cls.ttl_groups = config['cache_ttl_groups']
        cls.ttl_short = config['cache_ttl_short']
        cls.ttl_long = config['cache_ttl_long']

        max_entry_size = config['cache_size']['max_entry_size']
        cls.max_entry_size = utils.megs_to_bytes(max_entry_size)

        max_memory = config['cache_size']['max_memory']
        cls.max_memory = utils.megs_to_bytes(max_memory)

    # ------------------------------------------------------------------------------------ #
    def get(self, endpoint: str, params: dict) -> dict | None:
        key = utils.get_request_key(endpoint, params)
        entry = self.cache.get(key)
        if entry:
            if utils.is_expired(entry['exp_date']):
                self.remove_entry(key)
            else:
                self.cache.move_to_end(key, last=False)
                return json.loads(entry['response'])
        return None

    # ------------------------------------------------------------------------------------ #
    def set(self, endpoint: str, params: dict, response: dict) -> None:
        if ttl := self.get_ttl_value(endpoint):
            resp = json.dumps(response)
            size = utils.get_entry_size(resp)

            if self.is_entry_size_valid(size):  # pragma: no branch
                while self.is_space_full(size):
                    self.remove_entry()

                key = utils.get_request_key(endpoint, params)
                date = utils.get_expiration_date(ttl)
                self.cache[key] = dict(
                    size_of=size,
                    exp_date=date,
                    response=resp
                )
                self.cache.move_to_end(key, last=False)
                self.mem_in_use += size

    # ------------------------------------------------------------------------------------ #
    def get_ttl_value(self, endpoint: str) -> float:
        short = endpoint in self.ttl_short
        long = endpoint in self.ttl_long
        if self.ttl_groups['override']:
            ttl = {
                short: self.ttl_groups['short_ttl'],
                long: self.ttl_groups['long_ttl']
            }.get(True, 0.0)
        else:
            ttl = {
                short: self.ttl_short.get(endpoint),
                long: self.ttl_long.get(endpoint)
            }.get(True, 0.0)
        return float(ttl)

    # ------------------------------------------------------------------------------------ #
    def is_entry_size_valid(self, entry_size: int) -> bool:
        a = entry_size < self.max_entry_size
        b = entry_size < self.max_memory
        return a and b

    # ------------------------------------------------------------------------------------ #
    def is_space_full(self, entry_size: int) -> bool:
        if entry_size > (self.max_memory - self.mem_in_use):
            return True
        if len(self.cache) == self.max_entries:
            return True
        return False

    # ------------------------------------------------------------------------------------ #
    def remove_entry(self, key=None) -> None:
        if key is None:
            entry = self.cache.popitem(last=True)[1]
        else:
            entry = self.cache.pop(key)
        self.mem_in_use -= entry['size_of']
