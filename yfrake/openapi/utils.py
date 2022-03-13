# ================================================================================== #
#   utils.py - This file is part of the yfrake package.                              #
# ================================================================================== #
#                                                                                    #
#   MIT License                                                                      #
#                                                                                    #
#   Copyright (c) 2022 Mattias Aabmets                                               #
#                                                                                    #
#   Permission is hereby granted, free of charge, to any person obtaining a copy     #
#   of this software and associated documentation files (the "Software"), to deal    #
#   in the Software without restriction, including without limitation the rights     #
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell        #
#   copies of the Software, and to permit persons to whom the Software is            #
#   furnished to do so, subject to the following conditions:                         #
#                                                                                    #
#   The above copyright notice and this permission notice shall be included in all   #
#   copies or substantial portions of the Software.                                  #
#                                                                                    #
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR       #
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,         #
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE      #
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER           #
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,    #
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE    #
#   SOFTWARE.                                                                        #
#                                                                                    #
# ================================================================================== #
from pathlib import Path


# ================================================================================== #
def get_spec_file_path() -> Path:
    path = Path(__file__).resolve()
    return path.with_name('yfrake_spec.yaml')


# ---------------------------------------------------------------------------------- #
def get_toml_file_path() -> Path:
    path = Path(__file__).resolve()
    return path.parents[2].joinpath('pyproject.toml')


# ---------------------------------------------------------------------------------- #
def get_openapi_datatype(var: object) -> str:
    """
    Converts python datatype names into OpenAPI words.
    """
    default = ''
    _map = {
        'str': 'string',
        'int': 'integer',
        'bool': 'boolean',
        'list': 'array',
        'dict': 'object',
        'float': 'number',
    }
    if var.__class__.__name__ == 'type':
        return _map.get(var.__name__, default)
    return _map.get(var.__class__.__name__, default)
