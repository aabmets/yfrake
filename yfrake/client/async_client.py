# ==================================================================================== #
#    async_client.py - This file is part of the YFrake package.                        #
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
from .base_worker import BaseWorker
from .response import Response


# ==================================================================================== #
class AsyncClient(BaseWorker):
    """
    This class contains the public async 'get_' methods,
    which should be called in an async context by the
    user to request data from the Yahoo Finance API.
    """
    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_historical_prices(cls, **params) -> Response:
        endpoint: str = 'historical_prices'
        if 'startDate' in params:
            params['period1'] = params.pop('startDate')
        if 'endDate' in params:
            params['period2'] = params.pop('endDate')
        if 'extHours' in params:
            params['includePrePost'] = params.pop('extHours')
        if 'events' in params and params.pop('events'):
            params['events'] = 'div,split'
        params['includeAdjustedClose'] = 'true'
        resp = await cls._request(params, endpoint)
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['chart']['result'][0]
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
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_options(cls, **kwargs) -> Response:
        if 'startDate' in kwargs:
            kwargs['date'] = kwargs.pop('startDate')
        resp = await cls._request(kwargs, 'options')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['optionChain']['result'][0]
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_insights(cls, **kwargs) -> Response:
        resp = await cls._request(kwargs, 'insights')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['finance']['result']
            data.update(data.pop('instrumentInfo'))
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_quotes_overview(cls, **kwargs) -> Response:
        resp = await cls._request(kwargs, 'quotes_overview')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = {'list': resp.data['quoteResponse']['result']}
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_esg_chart(cls, **kwargs) -> Response:
        resp = await cls._request(kwargs, 'esg_chart')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['esgChart']['result'][0]
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_quote_type(cls, **kwargs) -> Response:
        resp = await cls._request(kwargs, 'quote_type')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['quoteType']['result'][0]
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_news(cls, **kwargs) -> Response:
        if 'symbol' in kwargs:
            kwargs['q'] = kwargs.pop('symbol')
        resp = await cls._request(kwargs, 'news')
        data: dict | None = resp.data
        if not resp.error:
            data = dict(list=resp.data['news'])
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_recommendations(cls, **kwargs) -> Response:
        resp = await cls._request(kwargs, 'recommendations')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['finance']['result'][0]
            data['recommendedPeers'] = data.pop('recommendedSymbols')
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_shares_outstanding(cls, **kwargs) -> Response:
        if 'startDate' in kwargs:
            kwargs['period1'] = kwargs.pop('startDate')
        if 'endDate' in kwargs:
            kwargs['period2'] = kwargs.pop('endDate')
        resp = await cls._request(kwargs, 'shares_outstanding')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['timeseries']['result'][0]
            data['symbol'] = data['meta']['symbol'][0]
            del data['meta']
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_validate_symbols(cls, **kwargs) -> Response:
        resp = await cls._request(kwargs, 'validate_symbols')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['symbolsValidation']['result'][0]
            _list = []
            for key in data.keys():
                _list.append({
                    'symbol': key,
                    'valid': data[key]
                })
            data = dict(list=_list)
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_market_summary(cls, **kwargs) -> Response:
        resp = await cls._request(kwargs, 'market_summary')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['marketSummaryResponse']['result']
            data = dict(list=data)
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_trending_symbols(cls, **kwargs) -> Response:
        resp = await cls._request(kwargs, 'trending_symbols')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['finance']['result'][0]['quotes']
            data = dict(list=data)
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_currencies(cls, **kwargs) -> Response:
        resp = await cls._request(kwargs, 'currencies')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['currencies']['result']
            for i, _ in enumerate(data):
                del data[i]['symbol']
                del data[i]['localLongName']
            data = dict(list=data)
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_esg_scores(cls, **kwargs) -> Response:
        kwargs['modules'] = 'esgScores'
        resp = await cls._request(kwargs, 'esg_scores')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['quoteSummary']['result'][0]['esgScores']
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_purchase_activity(cls, **kwargs) -> Response:
        kwargs['modules'] = 'netSharePurchaseActivity'
        resp = await cls._request(kwargs, 'purchase_activity')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['quoteSummary']['result'][0]['netSharePurchaseActivity']
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_earnings(cls, **kwargs) -> Response:
        kwargs['modules'] = 'earnings'
        resp = await cls._request(kwargs, 'earnings')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['quoteSummary']['result'][0]['earnings']
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_price_overview(cls, **kwargs) -> Response:
        kwargs['modules'] = 'price'
        resp = await cls._request(kwargs, 'price_overview')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['quoteSummary']['result'][0]['price']
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_calendar_events(cls, **kwargs) -> Response:
        kwargs['modules'] = 'calendarEvents'
        resp = await cls._request(kwargs, 'calendar_events')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['quoteSummary']['result'][0]['calendarEvents']
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_company_overview(cls, **kwargs) -> Response:
        kwargs['modules'] = 'assetProfile'
        resp = await cls._request(kwargs, 'company_overview')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['quoteSummary']['result'][0]['assetProfile']
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_sec_filings(cls, **kwargs) -> Response:
        kwargs['modules'] = 'secFilings'
        resp = await cls._request(kwargs, 'sec_filings')
        data: dict | None = resp.data
        if not resp.error:
            data = resp.data['quoteSummary']['result'][0]['secFilings']['filings']
            data = dict(list=data)
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_detailed_summary(cls, **kwargs) -> Response:
        kwargs['modules'] = 'summaryDetail'
        resp = await cls._request(kwargs, 'detailed_summary')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['quoteSummary']['result'][0]['summaryDetail']
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_financials(cls, **kwargs) -> Response:
        kwargs['modules'] = 'financialData'
        resp = await cls._request(kwargs, 'financials')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['quoteSummary']['result'][0]['financialData']
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_recommendation_trend(cls, **kwargs) -> Response:
        kwargs['modules'] = 'recommendationTrend'
        resp = await cls._request(kwargs, 'recommendation_trend')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['quoteSummary']['result'][0]['recommendationTrend']
            data = dict(list=data['trend'])
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_ratings_history(cls, **kwargs) -> Response:
        kwargs['modules'] = 'upgradeDowngradeHistory'
        resp = await cls._request(kwargs, 'ratings_history')
        data: dict | None = resp.data
        if not resp.error:
            data = resp.data['quoteSummary']['result'][0]['upgradeDowngradeHistory']
            data = dict(list=data['history'])
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_earnings_history(cls, **kwargs) -> Response:
        kwargs['modules'] = 'earningsHistory'
        resp = await cls._request(kwargs, 'earnings_history')
        data: dict | None = resp.data
        if not resp.error:
            data = resp.data['quoteSummary']['result'][0]['earningsHistory']
            data = dict(list=data['history'])
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_earnings_trend(cls, **kwargs) -> Response:
        kwargs['modules'] = 'earningsTrend'
        resp = await cls._request(kwargs, 'earnings_trend')
        data: dict | None = resp.data
        if not resp.error:
            data = resp.data['quoteSummary']['result'][0]['earningsTrend']
            data = dict(list=data['trend'])
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_key_stats(cls, **kwargs) -> Response:
        kwargs['modules'] = 'defaultKeyStatistics'
        resp = await cls._request(kwargs, 'key_stats')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['quoteSummary']['result'][0]['defaultKeyStatistics']
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_income_statements(cls, **kwargs) -> Response:
        kwargs['modules'] = 'incomeStatementHistory,incomeStatementHistoryQuarterly'
        resp = await cls._request(kwargs, 'income_statements')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['quoteSummary']['result'][0]
            data = dict(
                income_yearly=data['incomeStatementHistory']['incomeStatementHistory'],
                income_quarterly=data['incomeStatementHistoryQuarterly']['incomeStatementHistory']
            )
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_cashflow_statements(cls, **kwargs) -> Response:
        kwargs['modules'] = 'cashflowStatementHistory,cashflowStatementHistoryQuarterly'
        resp = await cls._request(kwargs, 'cashflow_statements')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['quoteSummary']['result'][0]
            data = dict(
                cashflow_yearly=data['cashflowStatementHistory']['cashflowStatements'],
                cashflow_quarterly=data['cashflowStatementHistoryQuarterly']['cashflowStatements']
            )
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_balance_statements(cls, **kwargs) -> Response:
        kwargs['modules'] = 'balanceSheetHistory,balanceSheetHistoryQuarterly'
        resp = await cls._request(kwargs, 'balance_statements')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['quoteSummary']['result'][0]
            data = dict(
                balance_yearly=data['balanceSheetHistory']['balanceSheetStatements'],
                balance_quarterly=data['balanceSheetHistoryQuarterly']['balanceSheetStatements']
            )
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_institution_ownership(cls, **kwargs) -> Response:
        kwargs['modules'] = 'institutionOwnership'
        resp = await cls._request(kwargs, 'institution_ownership')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['quoteSummary']['result'][0]['institutionOwnership']
            data = dict(list=data['ownershipList'])
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_fund_ownership(cls, **kwargs) -> Response:
        kwargs['modules'] = 'fundOwnership'
        resp = await cls._request(kwargs, 'fund_ownership')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['quoteSummary']['result'][0]['fundOwnership']
            data = dict(list=data['ownershipList'])
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_major_holders(cls, **kwargs) -> Response:
        kwargs['modules'] = 'majorHoldersBreakdown'
        resp = await cls._request(kwargs, 'major_holders')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['quoteSummary']['result'][0]['majorHoldersBreakdown']
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_insider_transactions(cls, **kwargs) -> Response:
        kwargs['modules'] = 'insiderTransactions'
        resp = await cls._request(kwargs, 'insider_transactions')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['quoteSummary']['result'][0]['insiderTransactions']
            data = dict(list=data['transactions'])
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )

    # ------------------------------------------------------------------------------------ #
    @classmethod
    async def get_insider_holders(cls, **kwargs) -> Response:
        kwargs['modules'] = 'insiderHolders'
        resp = await cls._request(kwargs, 'insider_holders')
        data: dict | None = resp.data
        if not resp.error:
            data: dict = resp.data['quoteSummary']['result'][0]['insiderHolders']
            data = dict(list=data['holders'])
        return Response(
            endpoint=resp.endpoint,
            error=resp.error,
            data=data
        )
