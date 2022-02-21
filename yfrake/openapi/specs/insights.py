# ================================================================================== #
#   insights.py - This file is part of the yfrake package.                           #
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
summary = 'Insights'
description = 'Returns the sentiment and valuation of a security identifier.'

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
    'symbol': str,
    'companySnapshot': {
        'sectorInfo': str,
        'company': {
            'innovativeness': float,
            'hiring': float,
            'sustainability': float,
            'insiderSentiments': float,
            'earningsReports': float,
            'dividends': float
        },
        'sector': {
            'innovativeness': float,
            'hiring': float,
            'sustainability': float,
            'insiderSentiments': float,
            'earningsReports': float,
            'dividends': float
        }
    },
    'recommendation': {
        'targetPrice': float,
        'provider': str,
        'rating': str
    },
    'sigDevs': [
        {
            'headline': str,
            'date': str
        }
    ],
    'technicalEvents': {
        'provider': str,
        'sector': str,
        'shortTermOutlook': {
            'stateDescription': str,
            'direction': str,
            'score': int,
            'scoreDescription': str,
            'sectorDirection': str,
            'sectorScore': int,
            'sectorScoreDescription': str,
            'indexDirection': str,
            'indexScore': int,
            'indexScoreDescription': str
        },
        'intermediateTermOutlook': {
            'stateDescription': str,
            'direction': str,
            'score': int,
            'scoreDescription': str,
            'sectorDirection': str,
            'sectorScore': int,
            'sectorScoreDescription': str,
            'indexDirection': str,
            'indexScore': int,
            'indexScoreDescription': str
        },
        'longTermOutlook': {
            'stateDescription': str,
            'direction': str,
            'score': int,
            'scoreDescription': str,
            'sectorDirection': str,
            'sectorScore': int,
            'sectorScoreDescription': str,
            'indexDirection': str,
            'indexScore': int,
            'indexScoreDescription': str
        }
    },
    'keyTechnicals': {
        'provider': str,
        'support': float,
        'resistance': float,
        'stopLoss': float
    },
    'valuation': {
        'color': float,
        'description': str,
        'discount': str,
        'relativeValue': str,
        'provider': str
    }
}
