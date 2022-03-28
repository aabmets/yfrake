# ==================================================================================== #
#    validators.py - This file is part of the YFrake package.                          #
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
from ..openapi.modules import param_specs
from .exceptions import BadRequestError
from . import paths


# ==================================================================================== #
_err_msg_0 = 'Invalid endpoint \'{0}\'! (YFrake)'
_err_msg_1 = 'Invalid query parameter \'{0}\' for endpoint \'{1}\'. (YFrake)'
_err_msg_2 = 'Invalid datatype \'{0}\' for query parameter \'{1}\' at endpoint \'{2}\'. (YFrake)'


# ==================================================================================== #
def validate_request(endpoint: str, params: dict) -> None:
    """
    This function ensures the validity of any params
    passed into the client 'get' method by the user.
    """
    spec = param_specs.get(endpoint)

    if endpoint not in paths.keys():
        msg = _err_msg_0.format(
            endpoint
        )
        raise NameError(msg)

    for param in params:
        if param not in spec:
            msg = _err_msg_1.format(
                param, endpoint
            )
            raise KeyError(msg)

    for name, expected in spec.items():
        if name in params:
            value = params.get(name)
            if not isinstance(value, expected):
                msg = _err_msg_2.format(
                    type(value).__name__, name, endpoint
                )
                raise TypeError(msg)


# ------------------------------------------------------------------------------------ #
async def validate_response(data: dict) -> None:
    """
    This function ensures that an empty response
    with a successful status code 200 is correctly
    recognized as an erroneous response.
    """
    endpoint, error, result = await extract_fields(data)
    failures = [
        await is_general_error(error, result),
        await is_nested_dict_empty(error, result),
        await is_insights_error(endpoint, result),
        await is_shares_out_error(endpoint, result)
    ].count(True)
    if failures:
        raise BadRequestError


# ------------------------------------------------------------------------------------ #
async def extract_fields(data: dict) -> tuple:
    endpoint, error, result = None, None, None
    n = len(data)
    match n:
        case n if n > 1:
            result = data.get('news')
        case n if n == 1:
            endpoint = list(data.keys())[0]
            error = data[endpoint].get('error')
            result = data[endpoint].get('result')
    return endpoint, error, result


# ------------------------------------------------------------------------------------ #
async def is_general_error(error, result) -> bool:
    return True if error or not result else False


# ------------------------------------------------------------------------------------ #
async def is_nested_dict_empty(*args) -> bool:
    for arg in args:
        if isinstance(arg, list):
            if arg and not arg[0]:
                return True
    return False


# ------------------------------------------------------------------------------------ #
async def is_insights_error(endpoint, result) -> bool:
    if endpoint == 'finance':
        if isinstance(result, dict):
            if len(result) == 2:
                return True
    return False


# ------------------------------------------------------------------------------------ #
async def is_shares_out_error(endpoint, result) -> bool:
    if endpoint == 'timeseries':
        if len(result[0]) == 1:
            return True
    return False
