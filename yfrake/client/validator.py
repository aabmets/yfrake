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
async def validate(data) -> bool:
    """
    This function ensures that an empty response
    with a successful status code 200 is correctly
    recognized as an erroneous response.
    """
    error, result = await extract_fields(data)
    failures = [
        await is_general_error(error, result),
        await is_nested_list_empty(error, result)
    ].count(True)
    return False if failures else True


# ------------------------------------------------------------------------------------ #
async def extract_fields(data: dict) -> tuple:
    error, result = None, None
    if isinstance(data, dict):
        if len(data) == 1:
            endpoint = list(data.keys())[0]
            error = data[endpoint].get('error')
            result = data[endpoint].get('result')
        if len(data) > 1:
            result = data.get('news')
    return error, result


# ------------------------------------------------------------------------------------ #
async def is_general_error(error, result) -> bool:
    if error or not result:
        return True
    return False


# ------------------------------------------------------------------------------------ #
async def is_nested_list_empty(*args) -> bool:
    for arg in args:
        if isinstance(arg, list):
            if arg and not arg[0]:
                return True
    return False
