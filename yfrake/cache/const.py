# ==================================================================================== #
#    const.py - This file is part of the YFrake package.                               #
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
DATE_FORMAT = '%Y-%m-%d-%H-%M-%S-%f'
DATE_STR_EXAMPLE = '2022-04-13-14-28-53-944556'

BYTES_OVERHEAD_PARTS = dict(
    request_key_size=113,
    entry_dict_size=216,
    size_of_key_size=56,
    exp_date_key_size=57,
    response_key_size=57,
    size_of_value_size=28,
    exp_date_value_size=75
)
BYTES_OVERHEAD = sum(BYTES_OVERHEAD_PARTS.values())  # 602 bytes

# Reference for the above calculation:
#
# cache[request_key] = dict(
#     size_of_key=size_of_value,
#     exp_date_key=exp_date_value,
#     response_key=response.__sizeof__()
# )
