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
    Each method of this class handles calls to and
    returns responses from a specific API endpoint.
    """
    # Separate methods with involved data juggling are required,
    # because the Yahoo Finance API is a convoluted mangled mess.

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_validate_symbols(endpoint, **kwargs) -> BaseResponse:
        data, error = await Worker.request(endpoint, kwargs)
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
    async def get_historical_prices(endpoint, **kwargs) -> BaseResponse:
        if start_date := kwargs.pop('startDate', None):
            kwargs['period1'] = start_date
        if end_date := kwargs.pop('endDate', None):
            kwargs['period2'] = end_date
        if ext_hours := kwargs.pop('extHours', None):
            kwargs['includePrePost'] = ext_hours
        if kwargs.pop('events', None):
            kwargs['events'] = 'div,split'
        kwargs['includeAdjustedClose'] = 'true'
        data, error = await Worker.request(endpoint, kwargs)
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
    async def get_options(endpoint, **kwargs) -> BaseResponse:
        if start_date := kwargs.pop('startDate', None):
            kwargs['date'] = start_date
        if straddle := kwargs.pop('straddle', None):
            kwargs['straddle'] = straddle
        if get_all_data := kwargs.pop('getAllData', None):
            kwargs['getAllData'] = get_all_data
        data, error = await Worker.request(endpoint, kwargs)
        if not error:
            data: dict = data['optionChain']['result'][0]
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_insights(endpoint, **kwargs) -> BaseResponse:
        data, error = await Worker.request(endpoint, kwargs)
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
    async def get_quotes_overview(endpoint, **kwargs) -> BaseResponse:
        data, error = await Worker.request(endpoint, kwargs)
        if not error:
            data: dict = {'list': data['quoteResponse']['result']}
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_esg_chart(endpoint, **kwargs) -> BaseResponse:
        data, error = await Worker.request(endpoint, kwargs)
        if not error:
            data: dict = data['esgChart']['result'][0]
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_quote_type(endpoint, **kwargs) -> BaseResponse:
        data, error = await Worker.request(endpoint, kwargs)
        if not error:
            data: dict = data['quoteType']['result'][0]
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_news(endpoint, **kwargs) -> BaseResponse:
        if 'symbol' in kwargs:
            kwargs['q'] = kwargs.pop('symbol')
        data, error = await Worker.request(endpoint, kwargs)
        if not error:
            data = dict(list=data['news'])
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_recommendations(endpoint, **kwargs) -> BaseResponse:
        data, error = await Worker.request(endpoint, kwargs)
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
    async def get_shares_outstanding(endpoint, **kwargs) -> BaseResponse:
        if 'startDate' in kwargs:
            kwargs['period1'] = kwargs.pop('startDate')
        if 'endDate' in kwargs:
            kwargs['period2'] = kwargs.pop('endDate')
        data, error = await Worker.request(endpoint, kwargs)
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
    async def get_market_summary(endpoint, **kwargs) -> BaseResponse:
        data, error = await Worker.request(endpoint, kwargs)
        if not error:  # pragma: no branch
            data: dict = data['marketSummaryResponse']['result']
            data = dict(list=data)
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_trending_symbols(endpoint, **kwargs) -> BaseResponse:
        data, error = await Worker.request(endpoint, kwargs)
        if not error:  # pragma: no branch
            data: dict = data['finance']['result'][0]['quotes']
            data = dict(list=data)
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_currencies(endpoint, **kwargs) -> BaseResponse:
        data, error = await Worker.request(endpoint, kwargs)
        if not error:  # pragma: no branch
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
    async def get_esg_scores(endpoint, **kwargs) -> BaseResponse:
        kwargs['modules'] = 'esgScores'
        data, error = await Worker.request(endpoint, kwargs)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['esgScores']
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_purchase_activity(endpoint, **kwargs) -> BaseResponse:
        kwargs['modules'] = 'netSharePurchaseActivity'
        data, error = await Worker.request(endpoint, kwargs)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['netSharePurchaseActivity']
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_earnings(endpoint, **kwargs) -> BaseResponse:
        kwargs['modules'] = 'earnings'
        data, error = await Worker.request(endpoint, kwargs)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['earnings']
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_price_overview(endpoint, **kwargs) -> BaseResponse:
        kwargs['modules'] = 'price'
        data, error = await Worker.request(endpoint, kwargs)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['price']
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_calendar_events(endpoint, **kwargs) -> BaseResponse:
        kwargs['modules'] = 'calendarEvents'
        data, error = await Worker.request(endpoint, kwargs)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['calendarEvents']
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_company_overview(endpoint, **kwargs) -> BaseResponse:
        kwargs['modules'] = 'assetProfile'
        data, error = await Worker.request(endpoint, kwargs)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['assetProfile']
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_sec_filings(endpoint, **kwargs) -> BaseResponse:
        kwargs['modules'] = 'secFilings'
        data, error = await Worker.request(endpoint, kwargs)
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
    async def get_detailed_summary(endpoint, **kwargs) -> BaseResponse:
        kwargs['modules'] = 'summaryDetail'
        data, error = await Worker.request(endpoint, kwargs)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['summaryDetail']
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_financials(endpoint, **kwargs) -> BaseResponse:
        kwargs['modules'] = 'financialData'
        data, error = await Worker.request(endpoint, kwargs)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['financialData']
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_recommendation_trend(endpoint, **kwargs) -> BaseResponse:
        kwargs['modules'] = 'recommendationTrend'
        data, error = await Worker.request(endpoint, kwargs)
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
    async def get_ratings_history(endpoint, **kwargs) -> BaseResponse:
        kwargs['modules'] = 'upgradeDowngradeHistory'
        data, error = await Worker.request(endpoint, kwargs)
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
    async def get_earnings_history(endpoint, **kwargs) -> BaseResponse:
        kwargs['modules'] = 'earningsHistory'
        data, error = await Worker.request(endpoint, kwargs)
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
    async def get_earnings_trend(endpoint, **kwargs) -> BaseResponse:
        kwargs['modules'] = 'earningsTrend'
        data, error = await Worker.request(endpoint, kwargs)
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
    async def get_key_stats(endpoint, **kwargs) -> BaseResponse:
        kwargs['modules'] = 'defaultKeyStatistics'
        data, error = await Worker.request(endpoint, kwargs)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['defaultKeyStatistics']
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_income_statements(endpoint, **kwargs) -> BaseResponse:
        kwargs['modules'] = 'incomeStatementHistory,incomeStatementHistoryQuarterly'
        data, error = await Worker.request(endpoint, kwargs)
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
    async def get_cashflow_statements(endpoint, **kwargs) -> BaseResponse:
        kwargs['modules'] = 'cashflowStatementHistory,cashflowStatementHistoryQuarterly'
        data, error = await Worker.request(endpoint, kwargs)
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
    async def get_balance_statements(endpoint, **kwargs) -> BaseResponse:
        kwargs['modules'] = 'balanceSheetHistory,balanceSheetHistoryQuarterly'
        data, error = await Worker.request(endpoint, kwargs)
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
    async def get_institution_ownership(endpoint, **kwargs) -> BaseResponse:
        kwargs['modules'] = 'institutionOwnership'
        data, error = await Worker.request(endpoint, kwargs)
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
    async def get_fund_ownership(endpoint, **kwargs) -> BaseResponse:
        kwargs['modules'] = 'fundOwnership'
        data, error = await Worker.request(endpoint, kwargs)
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
    async def get_major_holders(endpoint, **kwargs) -> BaseResponse:
        kwargs['modules'] = 'majorHoldersBreakdown'
        data, error = await Worker.request(endpoint, kwargs)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['majorHoldersBreakdown']
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @staticmethod
    async def get_insider_transactions(endpoint, **kwargs) -> BaseResponse:
        kwargs['modules'] = 'insiderTransactions'
        data, error = await Worker.request(endpoint, kwargs)
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
    async def get_insider_holders(endpoint, **kwargs) -> BaseResponse:
        kwargs['modules'] = 'insiderHolders'
        data, error = await Worker.request(endpoint, kwargs)
        if not error:
            data: dict = data['quoteSummary']['result'][0]['insiderHolders']
            data = dict(list=data['holders'])
        return BaseResponse(
            endpoint=endpoint,
            error=error,
            data=data
        )
