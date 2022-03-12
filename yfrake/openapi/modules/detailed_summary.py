# ================================================================================== #
#   detailed_summary.py - This file is part of the yfrake package.                   #
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
summary = 'Detailed Summary'
description = 'Returns the detailed summary of a security identifier.'

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
    'priceHint': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'previousClose': {
        'raw': float,
        'fmt': str
    },
    'open': {
        'raw': float,
        'fmt': str
    },
    'dayLow': {
        'raw': float,
        'fmt': str
    },
    'dayHigh': {
        'raw': float,
        'fmt': str
    },
    'regularMarketPreviousClose': {
        'raw': float,
        'fmt': str
    },
    'regularMarketOpen': {
        'raw': float,
        'fmt': str
    },
    'regularMarketDayLow': {
        'raw': float,
        'fmt': str
    },
    'regularMarketDayHigh': {
        'raw': float,
        'fmt': str
    },
    'dividendRate': {
        'raw': float,
        'fmt': str
    },
    'dividendYield': {
        'raw': float,
        'fmt': str
    },
    'exDividendDate': {
        'raw': int,
        'fmt': str
    },
    'payoutRatio': {
        'raw': float,
        'fmt': str
    },
    'fiveYearAvgDividendYield': {
        'raw': float,
        'fmt': str
    },
    'beta': {
        'raw': float,
        'fmt': str
    },
    'trailingPE': {
        'raw': float,
        'fmt': str
    },
    'forwardPE': {
        'raw': float,
        'fmt': str
    },
    'volume': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'regularMarketVolume': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'averageVolume': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'averageVolume10days': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'averageDailyVolume10Day': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'bid': {
        'raw': float,
        'fmt': str
    },
    'ask': {
        'raw': float,
        'fmt': str
    },
    'bidSize': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'askSize': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'marketCap': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'yield': dict,
    'ytdReturn': dict,
    'totalAssets': dict,
    'expireDate': dict,
    'strikePrice': dict,
    'openInterest': dict,
    'fiftyTwoWeekLow': {
        'raw': float,
        'fmt': str
    },
    'fiftyTwoWeekHigh': {
        'raw': float,
        'fmt': str
    },
    'priceToSalesTrailing12Months': {
        'raw': float,
        'fmt': str
    },
    'fiftyDayAverage': {
        'raw': float,
        'fmt': str
    },
    'twoHundredDayAverage': {
        'raw': float,
        'fmt': str
    },
    'trailingAnnualDividendRate': {
        'raw': float,
        'fmt': str
    },
    'trailingAnnualDividendYield': {
        'raw': float,
        'fmt': str
    },
    'navPrice': dict,
    'currency': str,
    'fromCurrency': str,
    'toCurrency': str,
    'lastMarket': str,
    'volume24Hr': dict,
    'volumeAllCurrencies': dict,
    'circulatingSupply': dict,
    'algorithm': str,
    'maxSupply': dict,
    'startDate': dict,
    'tradeable': bool
}
