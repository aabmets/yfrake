Overview
========

The standardized interface of the YFrake server simplifies the process of acquiring stock market data for other applications,
which can use their own networking libraries to make web requests to the YFrake server.

There are two ways how you can run the server: you can either control it from within your Python program
through the ``server`` singleton or you can directly call the YFrake module in the terminal with ``python -m yfrake args``.
When running the server from the terminal without any args, then nothing will happen.
The optional args are ``--run-server`` and ``--config-file /path``, which can be used independently from each other.

The arg ``--config-file`` accepts as its only parameter either a full path to the config file or the special keyword ``here``,
which will have the server look for the config file in the **Current Working Directory**.
When using the keyword ``here``, if the file does not exist, it will be created with the default settings.
If the parameter is a full path to a config file, then the file must exist, otherwise an exception will be thrown.
In all cases, the config file must be named ``yfrake_settings.ini``.

When ``--run-server`` is used without the ``--config-file`` arg, then the server is run with the default settings.
Using ``--config-file here`` without the ``--run-server`` arg is useful for getting a copy of the config file with the default settings to the **CWD**.

You can access the built-in Swagger documentation by running the server and
navigating to the servers root address in your web browser (default: ``http://localhost:8888``).

You can perform queries to the endpoints either directly through the Swagger Docs UI,
or by navigating to the appropriate URL-s in the address bar of your web browser.

When accessing endpoints through their URL-s, each endpoint has a path name like ``/market_summary``.
To request data from that endpoint, in your address bar you would write: ``http://localhost:8888/market_summary``.

If an endpoint like ``/company_overview`` requires query parameters, then you would write in your address bar:
``http://localhost:8888/company_overview?symbol=msft``.
