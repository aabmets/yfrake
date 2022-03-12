# ================================================================================== #
#   company_overview.py - This file is part of the yfrake package.                   #
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
summary = 'Company Overview'
description = 'Returns the company overview of a security identifier.'

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
    'address1': str,
    'city': str,
    'state': str,
    'zip': str,
    'country': str,
    'phone': str,
    'website': str,
    'industry': str,
    'sector': str,
    'longBusinessSummary': str,
    'fullTimeEmployees': int,
    'companyOfficers': [
        {
            'maxAge': int,
            'name': str,
            'age': int,
            'title': str,
            'yearBorn': int,
            'fiscalYear': int,
            'totalPay': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'exercisedValue': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            },
            'unexercisedValue': {
                'raw': int,
                'fmt': str,
                'longFmt': str
            }
        }
    ],
    'auditRisk': int,
    'boardRisk': int,
    'compensationRisk': int,
    'shareHolderRightsRisk': int,
    'overallRisk': int,
    'governanceEpochDate': int,
    'compensationAsOfEpochDate': int,
    'maxAge': int
}
