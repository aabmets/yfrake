# ================================================================================== #
#   balance_statements.py - This file is part of the yfrake package.                 #
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
summary = 'Balance Statements'
description = 'Returns the balance statements of a security identifier.'

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
    'balance_yearly': [
        {
            'maxAge': int,
            'endDate': {
                'raw': int,
                'fmt': str
            },
            'cash': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'shortTermInvestments': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'netReceivables': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'inventory': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'otherCurrentAssets': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'totalCurrentAssets': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'longTermInvestments': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'propertyPlantEquipment': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'goodWill': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'intangibleAssets': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'otherAssets': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'deferredLongTermAssetCharges': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'totalAssets': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'accountsPayable': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'shortLongTermDebt': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'otherCurrentLiab': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'longTermDebt': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'otherLiab': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'totalCurrentLiabilities': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'totalLiab': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'commonStock': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'retainedEarnings': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'treasuryStock': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'otherStockholderEquity': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'totalStockholderEquity': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'netTangibleAssets': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            }
        }
    ],
    'balance_quarterly': [
        {
            'maxAge': int,
            'endDate': {
                'raw': int,
                'fmt': str
            },
            'cash': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'shortTermInvestments': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'netReceivables': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'inventory': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'otherCurrentAssets': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'totalCurrentAssets': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'longTermInvestments': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'propertyPlantEquipment': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'goodWill': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'intangibleAssets': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'otherAssets': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'totalAssets': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'accountsPayable': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'shortLongTermDebt': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'otherCurrentLiab': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'longTermDebt': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'otherLiab': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'totalCurrentLiabilities': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'totalLiab': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'commonStock': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'retainedEarnings': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'treasuryStock': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'otherStockholderEquity': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'totalStockholderEquity': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'netTangibleAssets': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            }
        }
    ]
}
