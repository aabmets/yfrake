# ================================================================================== #
#   key_statistics.py - This file is part of the yfrake package.                     #
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
summary = 'Key Statistics'
description = 'Returns the key statistics of a security identifier.'

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
    'enterpriseValue': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'forwardPE': {
        'raw': float,
        'fmt': str
    },
    'profitMargins': {
        'raw': float,
        'fmt': str
    },
    'floatShares': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'sharesOutstanding': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'sharesShort': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'sharesShortPriorMonth': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'sharesShortPreviousMonthDate': {
        'raw': int,
        'fmt': str
    },
    'dateShortInterest': {
        'raw': int,
        'fmt': str
    },
    'sharesPercentSharesOut': {
        'raw': float,
        'fmt': str
    },
    'heldPercentInsiders': {
        'raw': float,
        'fmt': str
    },
    'heldPercentInstitutions': {
        'raw': float,
        'fmt': str
    },
    'shortRatio': {
        'raw': float,
        'fmt': str
    },
    'shortPercentOfFloat': {
        'raw': float,
        'fmt': str
    },
    'beta': {
        'raw': float,
        'fmt': str
    },
    'impliedSharesOutstanding': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'morningStarOverallRating': dict,
    'morningStarRiskRating': dict,
    'category': dict,
    'bookValue': {
        'raw': float,
        'fmt': str
    },
    'priceToBook': {
        'raw': float,
        'fmt': str
    },
    'annualReportExpenseRatio': dict,
    'ytdReturn': dict,
    'beta3Year': dict,
    'totalAssets': dict,
    'yield': dict,
    'fundFamily': dict,
    'fundInceptionDate': dict,
    'legalType': dict,
    'threeYearAverageReturn': dict,
    'fiveYearAverageReturn': dict,
    'priceToSalesTrailing12Months': dict,
    'lastFiscalYearEnd': {
        'raw': int,
        'fmt': str
    },
    'nextFiscalYearEnd': {
        'raw': int,
        'fmt': str
    },
    'mostRecentQuarter': {
        'raw': int,
        'fmt': str
    },
    'earningsQuarterlyGrowth': {
        'raw': float,
        'fmt': str
    },
    'revenueQuarterlyGrowth': dict,
    'netIncomeToCommon': {
        'raw': int,
        'fmt': str,
        'longFmt': str
    },
    'trailingEps': {
        'raw': float,
        'fmt': str
    },
    'forwardEps': {
        'raw': float,
        'fmt': str
    },
    'pegRatio': {
        'raw': float,
        'fmt': str
    },
    'lastSplitFactor': str,
    'lastSplitDate': {
        'raw': int,
        'fmt': str
    },
    'enterpriseToRevenue': {
        'raw': float,
        'fmt': str
    },
    'enterpriseToEbitda': {
        'raw': float,
        'fmt': str
    },
    '52WeekChange': {
        'raw': float,
        'fmt': str
    },
    'SandP52WeekChange': {
        'raw': float,
        'fmt': str
    },
    'lastDividendValue': {
        'raw': float,
        'fmt': str
    },
    'lastDividendDate': {
        'raw': int,
        'fmt': str
    },
    'lastCapGain': dict,
    'annualHoldingsTurnover': dict
}
