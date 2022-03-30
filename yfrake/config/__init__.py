# ================================================================================== #
#   __init__.py - This file is part of the yfrake package.                           #
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
config_file_name = 'yfrake_settings.ini'
valid_config = {
    'client': {
        'limit':     int(),
        'timeout':   int()
    },
    'server': {
        'host':      str(),
        'port':      int(),
        'backlog':   int()
    }
}

# NOT IMPLEMENTED YET / WORK IN PROGRESS
#
#     'cache_max_size': {
#         'num_of_items':   int(),
#         'memory_megs':    int()
#     },
#     'cache_ttl_variable': {
#         'historical_prices':       str(),
#     },
#     'cache_ttl_constant': {
#         'options':                 int(),
#         'insights':                int(),
#         'quotes_overview':         int(),
#         'esg_chart':               int(),
#         'quote_type':              int(),
#         'news':                    int(),
#         'recommendations':         int(),
#         'shares_outstanding':      int(),
#         'validate_symbols':        int(),
#         'market_summary':          int(),
#         'trending_symbols':        int(),
#         'currencies':              int(),
#         'esg_scores':              int(),
#         'purchase_activity':       int(),
#         'earnings':                int(),
#         'price_overview':          int(),
#         'calendar_events':         int(),
#         'company_overview':        int(),
#         'sec_filings':             int(),
#         'detailed_summary':        int(),
#         'financials':              int(),
#         'recommendation_trend':    int(),
#         'ratings_history':         int(),
#         'earnings_history':        int(),
#         'earnings_trend':          int(),
#         'key_statistics':          int(),
#         'income_statements':       int(),
#         'cashflow_statements':     int(),
#         'balance_statements':      int(),
#         'institution_ownership':   int(),
#         'fund_ownership':          int(),
#         'major_holders':           int(),
#         'insider_transactions':    int(),
#         'insider_holders':         int()
#     }
# }
