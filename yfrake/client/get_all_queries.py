# ==================================================================================== #
#    get_all_queries.py - This file is part of the YFrake package.                     #
# ------------------------------------------------------------------------------------ #
#                                                                                      #
#    MIT License                                                                       #
#                                                                                      #
#    Copyright (c) 2022 Mattias Aabmets                                                #
#                                                                                      #
#    Permission is hereby granted, free of charge, to any person obtaining a copy      #
#    of this software and associated documentation files (the "Software"), to deal     #
#    in the Software without restriction, including without limitation the rights      #
#    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell         #
#    copies of the Software, and to permit persons to whom the Software is             #
#    furnished to do so, subject to the following conditions:                          #
#                                                                                      #
#    The above copyright notice and this permission notice shall be included in all    #
#    copies or substantial portions of the Software.                                   #
#                                                                                      #
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR        #
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,          #
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE       #
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER            #
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,     #
#    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE     #
#    SOFTWARE.                                                                         #
#                                                                                      #
# ==================================================================================== #
class GetAllQueries:
    """
    This is a custom datatype factory which creates
    the list of queries for the 'get_all' method.
    """
    def __new__(cls, symbol) -> list:
        queries = [
            dict(endpoint='historical_prices', symbol=symbol, interval='1d', range='max', events=True, extHours=True),
            dict(endpoint='shares_outstanding', symbol=symbol, startDate=946728000, endDate=3162293065),
            dict(endpoint='options', symbol=symbol, getAllData=True),
            dict(endpoint='balance_statements', symbol=symbol),
            dict(endpoint='calendar_events', symbol=symbol),
            dict(endpoint='cashflow_statements', symbol=symbol),
            dict(endpoint='company_overview', symbol=symbol),
            dict(endpoint='detailed_summary', symbol=symbol),
            dict(endpoint='earnings', symbol=symbol),
            dict(endpoint='earnings_history', symbol=symbol),
            dict(endpoint='earnings_trend', symbol=symbol),
            dict(endpoint='esg_chart', symbol=symbol),
            dict(endpoint='esg_scores', symbol=symbol),
            dict(endpoint='financials', symbol=symbol),
            dict(endpoint='fund_ownership', symbol=symbol),
            dict(endpoint='income_statements', symbol=symbol),
            dict(endpoint='insider_holders', symbol=symbol),
            dict(endpoint='insider_transactions', symbol=symbol),
            dict(endpoint='insights', symbol=symbol),
            dict(endpoint='institution_ownership', symbol=symbol),
            dict(endpoint='key_statistics', symbol=symbol),
            dict(endpoint='major_holders', symbol=symbol),
            dict(endpoint='news', symbol=symbol),
            dict(endpoint='price_overview', symbol=symbol),
            dict(endpoint='purchase_activity', symbol=symbol),
            dict(endpoint='quote_type', symbol=symbol),
            dict(endpoint='quotes_overview', symbols=symbol),
            dict(endpoint='ratings_history', symbol=symbol),
            dict(endpoint='recommendation_trend', symbol=symbol),
            dict(endpoint='recommendations', symbol=symbol),
            dict(endpoint='sec_filings', symbol=symbol),
            dict(endpoint='validate_symbols', symbols=symbol)
        ]
        return queries
