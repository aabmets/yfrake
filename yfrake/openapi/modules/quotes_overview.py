# ================================================================================== #
#   quotes_overview.py - This file is part of the yfrake package.                    #
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
summary = 'Quotes Overview'
description = 'Returns the financial overviews of a list of security identifiers.'

# ---------------------------------------------------------------------------------- #
parameters = [
    {
        'name': 'symbols',
        'description': 'Comma-separated list of valid security identifiers.',
        'required': True,
        'in': 'query',
        'schema': {
            'type': str
        }
    }
]

# ---------------------------------------------------------------------------------- #
response = {
    'list': [
        {
            'language': str,
            'region': str,
            'quoteType': str,
            'quoteSourceName': str,
            'triggerable': bool,
            'currency': str,
            'postMarketChangePercent': float,
            'postMarketTime': int,
            'postMarketPrice': float,
            'postMarketChange': float,
            'regularMarketChange': float,
            'regularMarketChangePercent': float,
            'regularMarketTime': int,
            'regularMarketPrice': float,
            'regularMarketDayHigh': float,
            'regularMarketDayRange': str,
            'regularMarketDayLow': float,
            'regularMarketVolume': int,
            'regularMarketPreviousClose': float,
            'bid': float,
            'ask': float,
            'bidSize': int,
            'askSize': int,
            'fullExchangeName': str,
            'financialCurrency': str,
            'regularMarketOpen': float,
            'averageDailyVolume3Month': int,
            'averageDailyVolume10Day': int,
            'fiftyTwoWeekLowChange': float,
            'fiftyTwoWeekLowChangePercent': float,
            'fiftyTwoWeekRange': str,
            'fiftyTwoWeekHighChange': float,
            'fiftyTwoWeekHighChangePercent': float,
            'fiftyTwoWeekLow': float,
            'fiftyTwoWeekHigh': float,
            'dividendDate': int,
            'earningsTimestamp': int,
            'earningsTimestampStart': int,
            'earningsTimestampEnd': int,
            'trailingAnnualDividendRate': float,
            'trailingPE': float,
            'trailingAnnualDividendYield': float,
            'epsTrailingTwelveMonths': float,
            'epsForward': float,
            'epsCurrentYear': float,
            'priceEpsCurrentYear': float,
            'sharesOutstanding': int,
            'bookValue': float,
            'fiftyDayAverage': float,
            'fiftyDayAverageChange': float,
            'fiftyDayAverageChangePercent': float,
            'twoHundredDayAverage': float,
            'twoHundredDayAverageChange': float,
            'twoHundredDayAverageChangePercent': float,
            'marketCap': int,
            'forwardPE': float,
            'priceToBook': float,
            'sourceInterval': int,
            'exchangeDataDelayedBy': int,
            'pageViewGrowthWeekly': float,
            'averageAnalystRating': str,
            'tradeable': bool,
            'firstTradeDateMilliseconds': int,
            'priceHint': int,
            'exchangeTimezoneShortName': str,
            'gmtOffSetMilliseconds': int,
            'market': str,
            'esgPopulated': bool,
            'exchange': str,
            'shortName': str,
            'longName': str,
            'messageBoardId': str,
            'exchangeTimezoneName': str,
            'marketState': str,
            'displayName': str,
            'symbol': str
        }
    ]
}
