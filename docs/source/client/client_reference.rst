Client reference
================

.. py:decorator:: client.configure(limit=64, timeout=2)

   | Decorator, which manages the session for the YFrake client singleton.
   | It is recommended to decorate the *main* function or coroutine of your program.

   :param limit: The total number of concurrent requests to Yahoo Finance servers.
   :type limit: int

   :param timeout: Maximum allowed time per request to fetch data from Yahoo Finance servers, in seconds.
   :type timeout: int

   :raises RuntimeError: if a configuration is already active.

   :return: None


.. py:classmethod:: client.get(endpoint, **kwargs)

   | Schedules a request to be made to the Yahoo Finance servers.
   | Can be used anywhere in your code, if a configuration is active.

   :param endpoint: The name of the endpoint from which to request data.
   :type endpoint: str

   :param kwargs: Variable keyword arguments, which depend on the endpoint requirements. Values can be either *str*, *int* or *bool*.
   :type kwargs: unpacked dict

   :raises NameError: if an invalid endpoint name has been provided.

   :raises RuntimeError: if a configuration is not active.

   :return: Response object
   :rtype: ClientResponse
