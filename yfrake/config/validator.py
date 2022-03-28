# ==================================================================================== #
#    validator.py - This file is part of the YFrake package.                           #
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
from . import valid_config


# ==================================================================================== #
_err_msg_1 = 'Wrong or missing sections in the config file! (YFrake)'
_err_msg_2 = 'Wrong or missing fields in the config file! (YFrake)'
_err_msg_3 = 'Incorrect field type in the config file! (YFrake)'


# ==================================================================================== #
def validate_config(config: dict) -> None:
    for section in valid_config:
        test_section(config, section)
        for item in valid_config[section].items():
            test_item(config, section, item)

    for section in config:
        test_section(valid_config, section)
        for item in config[section].items():
            test_item(valid_config, section, item)


# ------------------------------------------------------------------------------------ #
def test_section(config, section) -> None:
    if section not in config:
        raise AttributeError(_err_msg_1)


# ------------------------------------------------------------------------------------ #
def test_item(config, section, item) -> None:
    key, value = item
    if key not in config[section]:
        raise KeyError(_err_msg_2)
    if not isinstance(config[section][key], type(value)):
        raise ValueError(_err_msg_3)
