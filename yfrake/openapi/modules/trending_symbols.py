# ================================================================================== #
#   trending_symbols.py - This file is part of the yfrake package.                   #
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
summary = 'Trending Symbols'
description = 'Returns a list of currently trending security identifiers.'

# ---------------------------------------------------------------------------------- #
parameters = [
    {
        'name': 'count',
        'description': 'Quantity of trending security identifiers to return.',
        'required': False,
        'in': 'query',
        'schema': {
            'type': int
        }
    }, {
        'name': 'useQuotes',
        'description': 'Option to include quotes data with the returned security identifiers.',
        'required': False,
        'in': 'query',
        'schema': {
            'type': bool
        }
    }
]

# ---------------------------------------------------------------------------------- #
response = {
    'list': [
        {
            'language': str,
            'region': str,
            'quoteType': str,
            'triggerable': bool,
            'quoteSourceName': str,
            'market': str,
            'fullExchangeName': str,
            'sourceInterval': int,
            'exchangeTimezoneName': str,
            'exchangeTimezoneShortName': str,
            'gmtOffSetMilliseconds': int,
            'esgPopulated': bool,
            'tradeable': bool,
            'priceHint': int,
            'exchange': str,
            'exchangeDataDelayedBy': int,
            'marketState': str,
            'symbol': str
        }
    ]
}
