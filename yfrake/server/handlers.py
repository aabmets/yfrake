# ==================================================================================== #
#    handlers.py - This file is part of the YFrake package.                            #
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
from ..client.async_client import AsyncClient
from ..server.utils import convert_multidict, pretty_json
from aiohttp.web import Request, Response


# ==================================================================================== #
class Handlers:
    """
    This class contains the endpoint functions
    of the http server app of this module.
    """
    @staticmethod
    async def handler_historical_prices(request: Request) -> Response:
        query: dict = convert_multidict(request.query)
        resp = await AsyncClient.get_historical_prices(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_options(request: Request) -> Response:
        query: dict = convert_multidict(request.query)
        resp = await AsyncClient.get_options(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_insights(request: Request) -> Response:
        query: dict = convert_multidict(request.query)
        resp = await AsyncClient.get_insights(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_quotes_overview(request: Request) -> Response:
        query: dict = convert_multidict(request.query)
        resp = await AsyncClient.get_quotes_overview(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_esg_chart(request: Request) -> Response:
        query: dict = convert_multidict(request.query)
        resp = await AsyncClient.get_esg_chart(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_quote_type(request: Request) -> Response:
        query: dict = convert_multidict(request.query)
        resp = await AsyncClient.get_quote_type(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_news(request: Request) -> Response:
        query: dict = convert_multidict(request.query)
        resp = await AsyncClient.get_news(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_recommendations(request: Request) -> Response:
        query: dict = convert_multidict(request.query)
        resp = await AsyncClient.get_recommendations(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_shares_outstanding(request: Request) -> Response:
        query: dict = convert_multidict(request.query)
        resp = await AsyncClient.get_shares_outstanding(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_validate_symbols(request: Request) -> Response:
        query: dict = convert_multidict(request.query)
        resp = await AsyncClient.get_validate_symbols(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_market_summary(request: Request) -> Response:
        query: dict = convert_multidict(request.query)
        resp = await AsyncClient.get_market_summary(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_trending_symbols(request: Request) -> Response:
        query: dict = convert_multidict(request.query)
        resp = await AsyncClient.get_trending_symbols(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_currencies(request: Request) -> Response:
        query = convert_multidict(request.query)
        resp = await AsyncClient.get_currencies(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_esg_scores(request: Request) -> Response:
        query = convert_multidict(request.query)
        resp = await AsyncClient.get_esg_scores(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_purchase_activity(request: Request) -> Response:
        query = convert_multidict(request.query)
        resp = await AsyncClient.get_purchase_activity(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_earnings(request: Request) -> Response:
        query = convert_multidict(request.query)
        resp = await AsyncClient.get_earnings(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_price_overview(request: Request) -> Response:
        query = convert_multidict(request.query)
        resp = await AsyncClient.get_price_overview(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_calendar_events(request: Request) -> Response:
        query = convert_multidict(request.query)
        resp = await AsyncClient.get_calendar_events(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_company_overview(request: Request) -> Response:
        query = convert_multidict(request.query)
        resp = await AsyncClient.get_company_overview(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_sec_filings(request: Request) -> Response:
        query = convert_multidict(request.query)
        resp = await AsyncClient.get_sec_filings(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_detailed_summary(request: Request) -> Response:
        query = convert_multidict(request.query)
        resp = await AsyncClient.get_detailed_summary(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_financials(request: Request) -> Response:
        query = convert_multidict(request.query)
        resp = await AsyncClient.get_financials(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_recommendation_trend(request: Request) -> Response:
        query = convert_multidict(request.query)
        resp = await AsyncClient.get_recommendation_trend(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_ratings_history(request: Request) -> Response:
        query = convert_multidict(request.query)
        resp = await AsyncClient.get_ratings_history(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_earnings_history(request: Request) -> Response:
        query = convert_multidict(request.query)
        resp = await AsyncClient.get_earnings_history(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_earnings_trend(request: Request) -> Response:
        query = convert_multidict(request.query)
        resp = await AsyncClient.get_earnings_trend(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_key_stats(request: Request) -> Response:
        query = convert_multidict(request.query)
        resp = await AsyncClient.get_key_stats(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_income_statements(request: Request) -> Response:
        query = convert_multidict(request.query)
        resp = await AsyncClient.get_income_statements(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_cashflow_statements(request: Request) -> Response:
        query = convert_multidict(request.query)
        resp = await AsyncClient.get_cashflow_statements(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_balance_statements(request: Request) -> Response:
        query = convert_multidict(request.query)
        resp = await AsyncClient.get_balance_statements(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_institution_ownership(request: Request) -> Response:
        query = convert_multidict(request.query)
        resp = await AsyncClient.get_institution_ownership(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_fund_ownership(request: Request) -> Response:
        query = convert_multidict(request.query)
        resp = await AsyncClient.get_fund_ownership(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_major_holders(request: Request) -> Response:
        query = convert_multidict(request.query)
        resp = await AsyncClient.get_major_holders(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_insider_transactions(request: Request) -> Response:
        query = convert_multidict(request.query)
        resp = await AsyncClient.get_insider_transactions(**query)
        return Response(text=pretty_json(resp))

    @staticmethod
    async def handler_insider_holders(request: Request) -> Response:
        query = convert_multidict(request.query)
        resp = await AsyncClient.get_insider_holders(**query)
        return Response(text=pretty_json(resp))
