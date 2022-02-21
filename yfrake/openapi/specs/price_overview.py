# ================================================================================== #
#   price_overview.py - This file is part of the yfrake package.                     #
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
summary = 'Price Overview'
description = 'Returns the price overview of a security identifier.'

# ---------------------------------------------------------------------------------- #
parameters = [
    {
        'name': 'symbol',
        'description': 'Any valid equity security identifier.',
        'required': True,
        'in': 'query',
        'schema': {
            'type': str
        }
    }
]

# ---------------------------------------------------------------------------------- #
response = {
    'maxAge': int,
    'preMarketChange': dict,
    'preMarketPrice': dict,
    'preMarketSource': str,
    'postMarketChangePercent': {
        'raw': float,
        'fmt': str
    },
    'postMarketChange': {
        'raw': float,
        'fmt': str
    },
    'postMarketTime': int,
    'postMarketPrice': {
        'raw': float,
        'fmt': str
    },
    'postMarketSource': str,
    'regularMarketChangePercent': {
        'raw': float,
        'fmt': str
    },
    'regularMarketChange': {
        'raw': float,
        'fmt': str
    },
    'regularMarketTime': int,
    'priceHint': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'regularMarketPrice': {
        'raw': float,
        'fmt': str
    },
    'regularMarketDayHigh': {
        'raw': float,
        'fmt': str
    },
    'regularMarketDayLow': {
        'raw': float,
        'fmt': str
    },
    'regularMarketVolume': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'averageDailyVolume10Day': dict,
    'averageDailyVolume3Month': dict,
    'regularMarketPreviousClose': {
        'raw': float,
        'fmt': str
    },
    'regularMarketSource': str,
    'regularMarketOpen': {
        'raw': float,
        'fmt': str
    },
    'strikePrice': dict,
    'openInterest': dict,
    'exchange': str,
    'exchangeName': str,
    'exchangeDataDelayedBy': int,
    'marketState': str,
    'quoteType': str,
    'symbol': str,
    'underlyingSymbol': str,
    'shortName': str,
    'longName': str,
    'currency': str,
    'quoteSourceName': str,
    'currencySymbol': str,
    'fromCurrency': str,
    'toCurrency': str,
    'lastMarket': str,
    'volume24Hr': dict,
    'volumeAllCurrencies': dict,
    'circulatingSupply': dict,
    'marketCap': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    }
}
