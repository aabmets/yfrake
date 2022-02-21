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
class InvalidResponseError(Exception):
    def __init__(self):
        self.status = 400
        self.message = 'Bad request'


# ==================================================================================== #
class Validator:
    @classmethod
    def validate(cls, data: dict) -> None:
        """
        This function ensures that an empty response
        with a successful status code 200 is correctly
        recognized as an erroneous response.
        """
        cls._check_special_case(data)
        error, result = cls._extract_fields(data)
        if error is not None or result is None:
            raise InvalidResponseError
        if isinstance(result, dict | list) and len(result) == 0:
            raise InvalidResponseError
        if isinstance(result, list) and result[0] == {}:
            raise InvalidResponseError

    # ------------------------------------------------------------------------------------ #
    @classmethod
    def _extract_fields(cls, data: dict) -> tuple:
        error, result = (True, False)
        if len(data) == 1:
            endpoint = list(data.keys())[0]
            error = data[endpoint].get('error')
            result = data[endpoint].get('result')
        return error, result

    # ------------------------------------------------------------------------------------ #
    @classmethod
    def _check_special_case(cls, data: dict) -> None:
        if len(data) > 1 and not data.get('news'):
            raise InvalidResponseError
