# ==================================================================================== #
#    paths.py - This file is part of the YFrake package.                               #
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
base_url: str = 'https://iquery.finance.yahoo.com'
paths: dict = {
    'historical_prices':        '/v8/finance/chart/{symbol}',
    'options':                  '/v7/finance/options/{symbol}',
    'insights':                 '/ws/insights/v2/finance/insights',
    'quotes_overview':          '/v7/finance/quote',
    'esg_chart':                '/v1/finance/esgChart',
    'quote_type':               '/v1/finance/quoteType/{symbol}',
    'news':                     '/v1/finance/search',
    'recommendations':          '/v6/finance/recommendationsbysymbol/{symbol}',
    'shares_outstanding':       '/ws/fundamentals-timeseries/v1/finance/timeseries/{symbol}',
    'validate_symbols':         '/v6/finance/quote/validate',
    'market_summary':           '/v6/finance/quote/marketSummary',
    'trending_symbols':         '/v1/finance/trending/US',
    'currencies':               '/v1/finance/currencies',
    'esg_scores':               '/v10/finance/quoteSummary/{symbol}',
    'purchase_activity':        '/v10/finance/quoteSummary/{symbol}',
    'earnings':                 '/v10/finance/quoteSummary/{symbol}',
    'price_overview':           '/v10/finance/quoteSummary/{symbol}',
    'calendar_events':          '/v10/finance/quoteSummary/{symbol}',
    'company_overview':         '/v10/finance/quoteSummary/{symbol}',
    'sec_filings':              '/v10/finance/quoteSummary/{symbol}',
    'detailed_summary':         '/v10/finance/quoteSummary/{symbol}',
    'financials':               '/v10/finance/quoteSummary/{symbol}',
    'recommendation_trend':     '/v10/finance/quoteSummary/{symbol}',
    'ratings_history':          '/v10/finance/quoteSummary/{symbol}',
    'earnings_history':         '/v10/finance/quoteSummary/{symbol}',
    'earnings_trend':           '/v10/finance/quoteSummary/{symbol}',
    'key_statistics':           '/v10/finance/quoteSummary/{symbol}',
    'income_statements':        '/v10/finance/quoteSummary/{symbol}',
    'cashflow_statements':      '/v10/finance/quoteSummary/{symbol}',
    'balance_statements':       '/v10/finance/quoteSummary/{symbol}',
    'institution_ownership':    '/v10/finance/quoteSummary/{symbol}',
    'fund_ownership':           '/v10/finance/quoteSummary/{symbol}',
    'major_holders':            '/v10/finance/quoteSummary/{symbol}',
    'insider_transactions':     '/v10/finance/quoteSummary/{symbol}',
    'insider_holders':          '/v10/finance/quoteSummary/{symbol}'
}
