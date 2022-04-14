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
    },
    'cache_size': {
        'max_entries':      int(),
        'max_entry_size':   int(),
        'max_memory':       int()
    },
    'cache_ttl_groups': {
        'override':    bool(),
        'short_ttl':   int(),
        'long_ttl':    int()
    },
    'cache_ttl_short': {
        'historical_prices':   int(),
        'detailed_summary':    int(),
        'financials':          int(),
        'insights':            int(),
        'key_statistics':      int(),
        'market_summary':      int(),
        'news':                int(),
        'options':             int(),
        'price_overview':      int(),
        'quotes_overview':     int(),
        'trending_symbols':    int()
    },
    'cache_ttl_long': {
        'balance_statements':      int(),
        'calendar_events':         int(),
        'cashflow_statements':     int(),
        'company_overview':        int(),
        'currencies':              int(),
        'earnings':                int(),
        'earnings_history':        int(),
        'earnings_trend':          int(),
        'esg_chart':               int(),
        'esg_scores':              int(),
        'fund_ownership':          int(),
        'income_statements':       int(),
        'insider_holders':         int(),
        'insider_transactions':    int(),
        'institution_ownership':   int(),
        'major_holders':           int(),
        'purchase_activity':       int(),
        'quote_type':              int(),
        'ratings_history':         int(),
        'recommendation_trend':    int(),
        'recommendations':         int(),
        'sec_filings':             int(),
        'shares_outstanding':      int(),
        'validate_symbols':        int()
    }
}
