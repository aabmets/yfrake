# ==================================================================================== #
#    endpoints.py - This file is part of the YFrake package.                           #
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
from .base_response import BaseResponse
from .worker import Worker


# ==================================================================================== #
class Endpoints:
    """
    This class contains the public async 'get_' methods,
    which should be called in an async context by the
    user to request data from the Yahoo Finance API.
    """
    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_historical_prices(**kwargs) -> BaseResponse:
        endpoint = 'historical_prices'
        if start_date := kwargs.pop('startDate', None):
            kwargs['period1'] = start_date
        if end_date := kwargs.pop('endDate', None):
            kwargs['period2'] = end_date
        if ext_hours := kwargs.pop('extHours', None):
            if type(ext_hours) is bool:
                kwargs['includePrePost'] = str(ext_hours).lower()
        if events := kwargs.pop('events', None):
            if type(events) is bool:
                kwargs['events'] = 'div,split'
        kwargs['includeAdjustedClose'] = 'true'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['chart']['result'][0]
            quotes: dict = data['indicators']['quote'][0]
            data['quotes'] = {
                'timestamp': data['timestamp'],
                'volume': quotes['volume'],
                'open': quotes['open'],
                'high': quotes['high'],
                'low': quotes['low'],
                'close': quotes['close']
            }
            if 'adjclose' in (i := data['indicators']):
                data['quotes']['adjclose'] = i['adjclose'][0]['adjclose']
            if 'events' not in data:
                data['events'] = {
                    'dividends': {},
                    'splits': {}
                }
            if 'tradingPeriods' in data['meta']:
                del data['meta']['tradingPeriods']
            del data['meta']['validRanges']
            del data['timestamp']
            del data['indicators']
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_options(**kwargs) -> BaseResponse:
        endpoint = 'options'
        if start_date := kwargs.pop('startDate', None):
            kwargs['date'] = start_date
        if straddle := kwargs.pop('straddle', None):
            if type(straddle) is bool:
                kwargs['straddle'] = str(straddle).lower()
        if get_all_data := kwargs.pop('getAllData', None):
            if type(get_all_data) is bool:
                kwargs['getAllData'] = str(get_all_data).lower()
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['optionChain']['result'][0]
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_insights(**kwargs) -> BaseResponse:
        endpoint = 'insights'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['finance']['result']
            data.update(data.pop('instrumentInfo'))
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_quotes_overview(**kwargs) -> BaseResponse:
        endpoint = 'quotes_overview'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = {'list': data['quoteResponse']['result']}
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_esg_chart(**kwargs) -> BaseResponse:
        endpoint = 'esg_chart'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['esgChart']['result'][0]
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_quote_type(**kwargs) -> BaseResponse:
        endpoint = 'quote_type'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['quoteType']['result'][0]
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_news(**kwargs) -> BaseResponse:
        endpoint = 'news'
        if 'symbol' in kwargs:
            kwargs['q'] = kwargs.pop('symbol')
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data = dict(list=data['news'])
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_recommendations(**kwargs) -> BaseResponse:
        endpoint = 'recommendations'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['finance']['result'][0]
            data['recommendedPeers'] = data.pop('recommendedSymbols')
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_shares_outstanding(**kwargs) -> BaseResponse:
        endpoint = 'shares_outstanding'
        if 'startDate' in kwargs:
            kwargs['period1'] = kwargs.pop('startDate')
        if 'endDate' in kwargs:
            kwargs['period2'] = kwargs.pop('endDate')
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['timeseries']['result'][0]
            data['symbol'] = data['meta']['symbol'][0]
            del data['meta']
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_validate_symbols(**kwargs) -> BaseResponse:
        endpoint = 'validate_symbols'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['symbolsValidation']['result'][0]
            _list = []
            for key in data.keys():
                _list.append({
                    'symbol': key,
                    'valid': data[key]
                })
            data = dict(list=_list)
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_market_summary(**kwargs) -> BaseResponse:
        endpoint = 'market_summary'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['marketSummaryResponse']['result']
            data = dict(list=data)
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_trending_symbols(**kwargs) -> BaseResponse:
        endpoint = 'trending_symbols'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['finance']['result'][0]['quotes']
            data = dict(list=data)
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_currencies(**kwargs) -> BaseResponse:
        endpoint = 'currencies'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['currencies']['result']
            for i, _ in enumerate(data):
                del data[i]['symbol']
                del data[i]['localLongName']
            data = dict(list=data)
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_esg_scores(**kwargs) -> BaseResponse:
        endpoint = 'esg_scores'
        kwargs['modules'] = 'esgScores'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['esgScores']
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_purchase_activity(**kwargs) -> BaseResponse:
        endpoint = 'purchase_activity'
        kwargs['modules'] = 'netSharePurchaseActivity'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['netSharePurchaseActivity']
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_earnings(**kwargs) -> BaseResponse:
        endpoint = 'earnings'
        kwargs['modules'] = 'earnings'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['earnings']
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_price_overview(**kwargs) -> BaseResponse:
        endpoint = 'price_overview'
        kwargs['modules'] = 'price'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['price']
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_calendar_events(**kwargs) -> BaseResponse:
        endpoint = 'calendar_events'
        kwargs['modules'] = 'calendarEvents'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['calendarEvents']
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_company_overview(**kwargs) -> BaseResponse:
        endpoint = 'company_overview'
        kwargs['modules'] = 'assetProfile'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['assetProfile']
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_sec_filings(**kwargs) -> BaseResponse:
        endpoint = 'sec_filings'
        kwargs['modules'] = 'secFilings'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data = data['quoteSummary']['result'][0]['secFilings']['filings']
            data = dict(list=data)
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_detailed_summary(**kwargs) -> BaseResponse:
        endpoint = 'detailed_summary'
        kwargs['modules'] = 'summaryDetail'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['summaryDetail']
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_financials(**kwargs) -> BaseResponse:
        endpoint = 'financials'
        kwargs['modules'] = 'financialData'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['financialData']
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_recommendation_trend(**kwargs) -> BaseResponse:
        endpoint = 'recommendation_trend'
        kwargs['modules'] = 'recommendationTrend'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['recommendationTrend']
            data = dict(list=data['trend'])
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_ratings_history(**kwargs) -> BaseResponse:
        endpoint = 'ratings_history'
        kwargs['modules'] = 'upgradeDowngradeHistory'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['upgradeDowngradeHistory']
            data = dict(list=data['history'])
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_earnings_history(**kwargs) -> BaseResponse:
        endpoint = 'earnings_history'
        kwargs['modules'] = 'earningsHistory'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['earningsHistory']
            data = dict(list=data['history'])
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_earnings_trend(**kwargs) -> BaseResponse:
        endpoint = 'earnings_trend'
        kwargs['modules'] = 'earningsTrend'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['earningsTrend']
            data = dict(list=data['trend'])
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_key_stats(**kwargs) -> BaseResponse:
        endpoint = 'key_stats'
        kwargs['modules'] = 'defaultKeyStatistics'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['defaultKeyStatistics']
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_income_statements(**kwargs) -> BaseResponse:
        endpoint = 'income_statements'
        kwargs['modules'] = 'incomeStatementHistory,incomeStatementHistoryQuarterly'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['quoteSummary']['result'][0]
            data = dict(
                income_yearly=data['incomeStatementHistory']['incomeStatementHistory'],
                income_quarterly=data['incomeStatementHistoryQuarterly']['incomeStatementHistory']
            )
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_cashflow_statements(**kwargs) -> BaseResponse:
        endpoint = 'cashflow_statements'
        kwargs['modules'] = 'cashflowStatementHistory,cashflowStatementHistoryQuarterly'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['quoteSummary']['result'][0]
            data = dict(
                cashflow_yearly=data['cashflowStatementHistory']['cashflowStatements'],
                cashflow_quarterly=data['cashflowStatementHistoryQuarterly']['cashflowStatements']
            )
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_balance_statements(**kwargs) -> BaseResponse:
        endpoint = 'balance_statements'
        kwargs['modules'] = 'balanceSheetHistory,balanceSheetHistoryQuarterly'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['quoteSummary']['result'][0]
            data = dict(
                balance_yearly=data['balanceSheetHistory']['balanceSheetStatements'],
                balance_quarterly=data['balanceSheetHistoryQuarterly']['balanceSheetStatements']
            )
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_institution_ownership(**kwargs) -> BaseResponse:
        endpoint = 'institution_ownership'
        kwargs['modules'] = 'institutionOwnership'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['institutionOwnership']
            data = dict(list=data['ownershipList'])
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_fund_ownership(**kwargs) -> BaseResponse:
        endpoint = 'fund_ownership'
        kwargs['modules'] = 'fundOwnership'
        data, error = await Worker.request(kwargs, endpoint)
        data: dict | None = data
        if not error:
            data: dict = data['quoteSummary']['result'][0]['fundOwnership']
            data = dict(list=data['ownershipList'])
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_major_holders(**kwargs) -> BaseResponse:
        endpoint = 'major_holders'
        kwargs['modules'] = 'majorHoldersBreakdown'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['majorHoldersBreakdown']
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_insider_transactions(**kwargs) -> BaseResponse:
        endpoint = 'insider_transactions'
        kwargs['modules'] = 'insiderTransactions'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['insiderTransactions']
            data = dict(list=data['transactions'])
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_insider_holders(**kwargs) -> BaseResponse:
        endpoint = 'insider_holders'
        kwargs['modules'] = 'insiderHolders'
        data, error = await Worker.request(kwargs, endpoint)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['insiderHolders']
            data = dict(list=data['holders'])
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )
