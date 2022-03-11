# This file contains the good queries for endpoint testing.

good_queries = [
    {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='historical_prices',
            symbol='msft',
            interval='1h',
            startDate=1609502400,
            endDate=1612180800,
            events=False,
            extHours=True
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='historical_prices',
            symbol='msft',
            interval='1wk',
            range='1y',
            events=True,
            extHours=False
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='options',
            symbol='msft',
            startDate=1609502400,
            endDate=1612180800,
            straddle=True,
            getAllData=False,
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='options',
            symbol='msft',
            startDate=1609502400,
            endDate=1612180800,
            straddle=False,
            getAllData=True,
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='shares_outstanding',
            symbol='msft',
            startDate=1609502400,
            endDate=1612180800
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='insights',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='quotes_overview',
            symbols='msft,aapl,tsla'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='esg_chart',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='quote_type',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='news',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='recommendations',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='validate_symbols',
            symbols='msft,aapl,tsla'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='market_summary'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='trending_symbols'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='currencies'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='esg_scores',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='purchase_activity',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='earnings',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='price_overview',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='calendar_events',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='company_overview',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='sec_filings',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='detailed_summary',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='financials',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='recommendation_trend',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='ratings_history',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='earnings_history',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='earnings_trend',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='key_stats',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='income_statements',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='cashflow_statements',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='balance_statements',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='institution_ownership',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='fund_ownership',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='major_holders',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='insider_transactions',
            symbol='msft'
        )
    }, {
        'expected_error': False,
        'expected_data': True,
        'query': dict(
            endpoint='insider_holders',
            symbol='msft'
        )
    }
]
