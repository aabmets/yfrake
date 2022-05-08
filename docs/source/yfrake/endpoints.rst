Endpoints
=========

| While all symbol-specific endpoints accept stock tickers,
| the following endpoints also accept forex and crypto tickers:

* historical_prices
* quotes_overview
* quote_type
* news
* recommendations
* validate_symbols


You can get the list of all valid endpoints and their arguments
by running the server and reading the Swagger documentation.
To convert the servers endpoint path param names for use with the client object,
just omit the ``/`` character from the beginning of the endpoint name:
``/company_overview`` becomes ``company_overview``.