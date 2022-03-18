Client Reference
================


.. contents:: Contents

.. raw:: html

   <br />
   <hr>


Public Decorators
-----------------

.. py:decorator:: configure(limit=64, timeout=2)

   | Manages the connection session for the YFrake client singleton.
   | Needs to be active when methods of the client object are being called.

   :param limit: The total number of concurrent requests to the Yahoo Finance API servers.
   :type limit: int

   :param timeout: The maximum time allowed for a request to fetch data from the Yahoo Finance API servers, in seconds.
   :type timeout: int

   :raises RuntimeError: if a configuration is already active.
   :raises RuntimeError: if a response or a results object has not been (a)waited when the decorated function or a coroutine finishes running.

   :return: None


.. raw:: html

   <br />
   <hr>


Public Methods
--------------

.. py:classmethod:: get(endpoint, **kwargs)

   | Schedules a request to be made to the Yahoo Finance servers.
   | Returns immediately with the pending response object.

   :param endpoint: The name of the endpoint from which to request data.
   :type endpoint: str

   :param kwargs: Variable keyword arguments, which depend on the endpoint requirements. Values can be either *str*, *int* or *bool*.
   :type kwargs: unpacked dict

   :raises RuntimeError: if a configuration is not active.
   :raises NameError: if an invalid endpoint name has been provided.
   :raises KeyError: if an invalid query parameter has been provided.
   :raises TypeError: if the datatype of a query parameter is invalid.

   :return: Response object
   :rtype: ClientResponse


.. py:classmethod:: batch_get(queries)

   | Helper method which schedules multiple queries at once.
   | Returns immediately with the pending results object.

   :param queries: Collection of query dicts.
   :type queries: list

   :raises RuntimeError: if a configuration is not active.
   :raises NameError: if an invalid endpoint name has been provided.
   :raises KeyError: if an invalid query parameter has been provided.
   :raises TypeError: if the datatype of a query parameter is invalid.
   :raises TypeError: if an element in the queries list is not a dict.

   :return: List-like collection object
   :rtype: AsyncResults or ThreadResults


.. py:classmethod:: get_all(symbol)

   | Helper method which schedules a request to all symbol-specific
   | endpoints for a given symbol at once. A single call results in
   | 32 simultaneous requests to the Yahoo Finance API servers.
   | Size of the returned data can vary from 1 to 1.5 megabytes.
   | Returns immediately with the pending results object.

   :param symbol: Security identifier.
   :type symbol: str

   :raises RuntimeError: if a configuration is not active.
   :raises NameError: if an invalid endpoint name has been provided.
   :raises KeyError: if an invalid query parameter has been provided.
   :raises TypeError: if the datatype of a query parameter is invalid.
   :raises TypeError: if an element in the queries list is not a dict.

   :return: List-like collection object
   :rtype: AsyncResults or ThreadResults
