# ==================================================================================== #
#    helpers.py - This file is part of the YFrake package.                             #
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
from .validator import validate_config
from configparser import ConfigParser
from pathlib import Path


# ==================================================================================== #
def read_config_from(path: Path | str) -> dict:
    cp = ConfigParser()
    cp.read(path)
    config = convert_to_dict(cp)
    config = convert_datatypes(config)
    validate_config(config)
    return config


# ------------------------------------------------------------------------------------ #
def convert_to_dict(cp: ConfigParser) -> dict:
    config = dict()
    for section in cp.sections():
        sect = section.lower()
        config[section.lower()] = dict()
        for key, value in cp.items(section):
            config[sect][key] = value
    return config


# ------------------------------------------------------------------------------------ #
def convert_datatypes(config: dict) -> dict:
    bool_map = dict(true=True, false=False)
    for section in config.values():
        for key, value in section.items():
            try:
                section[key] = int(value)
            except ValueError:
                section[key] = bool_map.get(value, value)
    return config
