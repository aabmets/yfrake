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
from . import config_file_name
from argparse import ArgumentParser
from configparser import ConfigParser
from pathlib import Path
import shutil
import os


# ==================================================================================== #
def convert_to_dict(cp: ConfigParser) -> dict:
    config = dict()
    for section in cp.sections():
        sect = section.lower()
        config[section.lower()] = dict()
        for key, value in cp.items(section):
            try:
                value = int(value)
            except ValueError:
                pass
            config[sect][key] = value
    return config


# ------------------------------------------------------------------------------------ #
def get_runtime_args() -> dict:  # pragma: no cover
    default = get_default_config_path()
    parser = ArgumentParser()
    parser.add_argument('--run-server', action='store_true', default=False)
    parser.add_argument('--config-file', type=str, default=str(default))
    ns = parser.parse_args()
    return dict(
        run_server=ns.run_server,
        config_file=ns.config_file
    )


# ------------------------------------------------------------------------------------ #
def get_default_config_path() -> Path:
    return Path(__file__).with_name(config_file_name).resolve()


# ------------------------------------------------------------------------------------ #
def get_cwd_config_path() -> Path:
    return Path(os.getcwd()).joinpath(config_file_name).resolve()


# ------------------------------------------------------------------------------------ #
def copy_default_config_to(dest: Path) -> None:
    default_config = get_default_config_path()
    shutil.copy(default_config, dest)



