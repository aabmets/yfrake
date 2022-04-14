Description
===========

YFrake is a fast and flexible stock market data scraper and server [#f1]_.
It enables developers to **build powerful apps** without having to worry about the details of session management or maximizing throughput [#f2]_.

YFrake has caching built in to speed up requests even more and to reduce load on the source servers.
The cache and other YFrake options are fully customizable through the configuration file.

YFrake can be used as a client to directly return market data to the current program or
as a **programmatically controllable server** to provide market data to other applications.

In addition, all network requests by the client in **both** sync and async modes are **non-blocking**,
which means that your program can continue executing your code while network requests are in progress.

The best part about YFrake is its **built-in swagger API documentation** which you can use to
perform test queries and examine the returned responses straight in your web browser.

YFrake is built upon the widely used **aiohttp** package and its plugins.

.. raw:: html

   <br />

.. [#f1] Stock market data is sourced from Yahoo Finance.
.. [#f2] The limits of YFrake are configurable and depend on the capabilities of your system.