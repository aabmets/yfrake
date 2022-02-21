# ================================================================================== #
#   financials.py - This file is part of the yfrake package.                         #
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
summary = 'Financials'
description = 'Returns the financials of a security identifier.'

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
    'currentPrice': {
        'raw': float,
        'fmt': str
    },
    'targetHighPrice': {
        'raw': float,
        'fmt': str
    },
    'targetLowPrice': {
        'raw': float,
        'fmt': str
    },
    'targetMeanPrice': {
        'raw': float,
        'fmt': str
    },
    'targetMedianPrice': {
        'raw': float,
        'fmt': str
    },
    'recommendationMean': {
        'raw': float,
        'fmt': str
    },
    'recommendationKey': str,
    'numberOfAnalystOpinions': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'totalCash': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'totalCashPerShare': {
        'raw': float,
        'fmt': str
    },
    'ebitda': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'totalDebt': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'quickRatio': {
        'raw': float,
        'fmt': str
    },
    'currentRatio': {
        'raw': float,
        'fmt': str
    },
    'totalRevenue': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'debtToEquity': {
        'raw': float,
        'fmt': str
    },
    'revenuePerShare': {
        'raw': float,
        'fmt': str
    },
    'returnOnAssets': {
        'raw': float,
        'fmt': str
    },
    'returnOnEquity': {
        'raw': float,
        'fmt': str
    },
    'grossProfits': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'freeCashflow': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'operatingCashflow': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'earningsGrowth': {
        'raw': float,
        'fmt': str
    },
    'revenueGrowth': {
        'raw': float,
        'fmt': str
    },
    'grossMargins': {
        'raw': float,
        'fmt': str
    },
    'ebitdaMargins': {
        'raw': float,
        'fmt': str
    },
    'operatingMargins': {
        'raw': float,
        'fmt': str
    },
    'profitMargins': {
        'raw': float,
        'fmt': str
    },
    'financialCurrency': str
}
