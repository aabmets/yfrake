# ================================================================================== #
#   cashflow_statements.py - This file is part of the yfrake package.                #
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
summary = 'Cashflow Statements'
description = 'Returns the cashflow statements of a security identifier.'

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
    'cashflow_yearly': [
        {
            'maxAge': int,
            'endDate': {
                'raw': int,
                'fmt': str
            },
            'netIncome': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'depreciation': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'changeToNetincome': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'changeToAccountReceivables': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'changeToLiabilities': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'changeToInventory': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'changeToOperatingActivities': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'totalCashFromOperatingActivities': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'capitalExpenditures': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'investments': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'otherCashflowsFromInvestingActivities': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'totalCashflowsFromInvestingActivities': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'dividendsPaid': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'netBorrowings': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'otherCashflowsFromFinancingActivities': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'totalCashFromFinancingActivities': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'effectOfExchangeRate': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'changeInCash': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'repurchaseOfStock': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'issuanceOfStock': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            }
        }
    ],
    'cashflow_quarterly': [
        {
            'maxAge': int,
            'endDate': {
                'raw': int,
                'fmt': str
            },
            'netIncome': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'depreciation': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'changeToNetincome': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'changeToAccountReceivables': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'changeToLiabilities': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'changeToInventory': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'changeToOperatingActivities': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'totalCashFromOperatingActivities': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'capitalExpenditures': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'investments': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'otherCashflowsFromInvestingActivities': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'totalCashflowsFromInvestingActivities': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'dividendsPaid': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'otherCashflowsFromFinancingActivities': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'totalCashFromFinancingActivities': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'effectOfExchangeRate': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'changeInCash': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'repurchaseOfStock': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'issuanceOfStock': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            }
        }
    ]
}
