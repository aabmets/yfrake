# This file contains the bad queries for endpoint testing.

bad_queries = [
    {
       'expected_error': True,
       'expected_data': False,
       'query': dict(
           endpoint='validate_symbols',
           symbols=''
       )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='historical_prices',
            symbol='qwerty123456',
            interval='1h',
            startDate=1609502400,
            endDate=1612180800,
            events=False,
            extHours=True
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='historical_prices',
            symbol='qwerty123456',
            interval='1wk',
            range='1y'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='options',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='options',
            symbol='qwerty123456',
            startDate=1609502400,
            endDate=1612180800,
            straddle=False,
            getAllData=True,
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='shares_outstanding',
            symbol='qwerty123456',
            startDate=1609502400,
            endDate=1612180800
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='shares_outstanding',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='insights',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='quotes_overview',
            symbols='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='esg_chart',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='quote_type',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='news'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='recommendations',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='esg_scores',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='purchase_activity',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='earnings',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='price_overview',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='calendar_events',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='company_overview',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='sec_filings',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='detailed_summary',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='financials',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='recommendation_trend',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='ratings_history',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='earnings_history',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='earnings_trend',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='key_stats',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='income_statements',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='cashflow_statements',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='balance_statements',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='institution_ownership',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='fund_ownership',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='major_holders',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='insider_transactions',
            symbol='qwerty123456'
        )
    }, {
        'expected_error': True,
        'expected_data': False,
        'query': dict(
            endpoint='insider_holders',
            symbol='qwerty123456'
        )
    }
]
