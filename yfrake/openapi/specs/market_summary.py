# ================================================================================== #
#   market_summary.py - This file is part of the yfrake package.                     #
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
summary = 'Market Summary'
description = 'Returns information about stock market exchanges.'

# ---------------------------------------------------------------------------------- #
parameters = []

# ---------------------------------------------------------------------------------- #
response = {
    'list': [
        {
            'fullExchangeName': str,
            'symbol': str,
            'headSymbolAsString': str,
            'gmtOffSetMilliseconds': int,
            'language': str,
            'regularMarketTime': {
                'raw': int,
                'fmt': str
            },
            'regularMarketChangePercent': {
                'raw': float,
                'fmt': str
            },
            'headSymbol': bool,
            'quoteType': str,
            'tradeable': bool,
            'contractSymbol': bool,
            'regularMarketPreviousClose': {
                'raw': float,
                'fmt': str
            },
            'exchangeTimezoneName': str,
            'regularMarketChange': {
                'raw': float,
                'fmt': str
            },
            'firstTradeDateMilliseconds': int,
            'exchangeDataDelayedBy': int,
            'exchangeTimezoneShortName': str,
            'marketState': str,
            'regularMarketPrice': {
                'raw': float,
                'fmt': str
            },
            'market': str,
            'sourceInterval': int,
            'exchange': str,
            'shortName': str,
            'region': str,
            'triggerable': bool
        }
    ]
}
