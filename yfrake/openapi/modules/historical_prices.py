# ================================================================================== #
#   historical_prices.py - This file is part of the yfrake package.                  #
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
summary = 'Historical Prices'
description = 'Returns historical prices of a security identifier.'

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
    }, {
        'name': 'interval',
        'description': 'Time granularity of the returned data points.',
        'required': True,
        'in': 'query',
        'schema': {
            'type': str,
            'enum': ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']
        }
    }, {
        'name': 'range',
        'description': 'Time span of the returned data points.',
        'required': False,
        'in': 'query',
        'schema': {
            'type': str,
            'enum': ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
        }
    }, {
        'name': 'startDate',
        'description': 'Start date encoded as an UNIX epoch timestamp.',
        'required': False,
        'in': 'query',
        'schema': {
            'type': int
        }
    }, {
        'name': 'endDate',
        'description': 'End date encoded as an UNIX epoch timestamp.',
        'required': False,
        'in': 'query',
        'schema': {
            'type': int
        }
    }, {
        'name': 'numberOfPoints',
        'description': 'Quantity of data points from start date.',
        'required': False,
        'in': 'query',
        'schema': {
            'type': int
        }
    }, {
        'name': 'events',
        'description': 'Option to include dividends and splits.',
        'required': False,
        'in': 'query',
        'schema': {
            'type': bool
        }
    }, {
        'name': 'extHours',
        'description': 'Option to include extended hours prices.',
        'required': False,
        'in': 'query',
        'schema': {
            'type': bool
        }
    }
]

# ---------------------------------------------------------------------------------- #
response = {
    'meta': {
        'currency': str,
        'symbol': str,
        'exchangeName': str,
        'instrumentType': str,
        'firstTradeDate': int,
        'regularMarketTime': int,
        'gmtoffset': int,
        'timezone': str,
        'exchangeTimezoneName': str,
        'regularMarketPrice': float,
        'chartPreviousClose': float,
        'priceHint': int,
        'currentTradingPeriod': {
            'pre': {
                'timezone': str,
                'start': int,
                'end': int,
                'gmtoffset': int
            },
            'regular': {
                'timezone': str,
                'start': int,
                'end': int,
                'gmtoffset': int
            },
            "post": {
                "timezone": str,
                "start": int,
                "end": int,
                "gmtoffset": int
            }
        },
        'dataGranularity': str,
        'range': str,
        'validRanges': list
    },
    'events': {
        'dividends': dict,
        'splits': dict
    },
    'quotes': {
        'timestamp': list,
        'volume': list,
        'open': list,
        'high': list,
        'low': list,
        'close': list,
        'adjclose': list
    }
}
