Client Reference
================


.. contents:: Contents

.. raw:: html

   <br />
   <hr>


Public Decorators
-----------------

.. py:decorator:: session

   | Manages the connection session for the YFrake client singleton.
   | Needs to be active when methods of the client object are being called.
   | The server object uses this decorator internally to manage its session
   | to the Yahoo Finance API servers.

   :raises RuntimeError: if a configuration is already active.


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

   :raises RuntimeError: if the session decorator is not in use.
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

   :raises RuntimeError: if the session decorator is not in use.
   :raises NameError: if an invalid endpoint name has been provided.
   :raises KeyError: if an invalid query parameter has been provided.
   :raises TypeError: if the datatype of a query parameter is invalid.

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

   :raises RuntimeError: if the session decorator is not in use.
   :raises NameError: if an invalid endpoint name has been provided.
   :raises KeyError: if an invalid query parameter has been provided.
   :raises TypeError: if the datatype of a query parameter is invalid.

   :return: List-like collection object
   :rtype: AsyncResults or ThreadResults
