# ================================================================================== #
#   income_statements.py - This file is part of the yfrake package.                  #
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
summary = 'Income Statements'
description = 'Returns the income statements of a security identifier.'

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
    'income_yearly': [
        {
            'maxAge': int,
            'endDate': {
                'raw': int,
                'fmt': str
            },
            'totalRevenue': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'costOfRevenue': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'grossProfit': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'researchDevelopment': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'sellingGeneralAdministrative': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'nonRecurring': dict,
            'otherOperatingExpenses': dict,
            'totalOperatingExpenses': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'operatingIncome': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'totalOtherIncomeExpenseNet': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'ebit': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'interestExpense': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'incomeBeforeTax': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'incomeTaxExpense': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'minorityInterest': dict,
            'netIncomeFromContinuingOps': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'discontinuedOperations': dict,
            'extraordinaryItems': dict,
            'effectOfAccountingCharges': dict,
            'otherItems': dict,
            'netIncome': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'netIncomeApplicableToCommonShares': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            }
        }
    ],
    'income_quarterly': [
        {
            'maxAge': int,
            'endDate': {
                'raw': int,
                'fmt': str
            },
            'totalRevenue': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'costOfRevenue': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'grossProfit': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'researchDevelopment': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'sellingGeneralAdministrative': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'nonRecurring': dict,
            'otherOperatingExpenses': dict,
            'totalOperatingExpenses': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'operatingIncome': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'totalOtherIncomeExpenseNet': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'ebit': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'interestExpense': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'incomeBeforeTax': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'incomeTaxExpense': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'minorityInterest': dict,
            'netIncomeFromContinuingOps': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'discontinuedOperations': dict,
            'extraordinaryItems': dict,
            'effectOfAccountingCharges': dict,
            'otherItems': dict,
            'netIncome': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'netIncomeApplicableToCommonShares': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            }
        }
    ]
}
