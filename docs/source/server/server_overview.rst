Overview
========

The standardized interface of the YFrake server simplifies the process of acquiring stock market data from other applications,
which can use their own networking libraries to make web requests to the YFrake server.

There are two ways how you can run the server: you can either control it from within your Python program or
you can run the ``runner.py`` module located in the ``/Libs/site-packages/yfrake/server`` folder of your Python distribution.

You can access the built-in Swagger documentation by running the server and
navigating to the servers root address in your web browser (default: ``localhost:8888``).

Each endpoint has a path name like ``/market_summary``, so to request data from that endpoint,
in your address bar you would write: ``localhost:8888/market_summary``.

If an endpoint like ``/company_overview`` requires query parameters, then you would write in your address bar:
``localhost:8888/company_overview?symbol=msft``.
