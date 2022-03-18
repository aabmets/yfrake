ClientResponse Reference
========================


.. contents:: Contents

.. raw:: html

   <br />
   <hr>


Public Methods
--------------

.. py:method:: pending()

   | Checks if the request has completed by calling the ``is_set()`` method on the
   | internal event object. Returns ``True`` if the request is still in progress.

   :return: Request completion status
   :rtype: bool


.. py:method:: wait()

   | In async mode, returns the ``wait()`` coroutine of the internal `asyncio.Event`_ object.
   | In sync (threaded) mode, calls the ``wait()`` method on the internal `threading.Event`_ object.

   :return: Awaitable coroutine or None
   :rtype: Coroutine or None


.. raw:: html

   <br />
   <hr>


API Response Properties
-----------------------

.. py:property:: endpoint

   | Provides access to the endpoint name of the response.

   :raises RuntimeError: on property modification or deletion.

   :return: Name of the endpoint.
   :rtype: str


.. py:property:: error

   | Provides access to the error dictionary of the response.

   :raises RuntimeError: on property modification or deletion.

   :return: Error dict, if there was an error, or None.
   :rtype: dict or None


.. py:property:: data

   | Provides access to the data dictionary of the response.

   :raises RuntimeError: on property modification or deletion.

   :return: Data dict, if there weren't any errors, or None.
   :rtype: dict or None


.. raw:: html

   <br />
   <hr>


Internal Request Properties
---------------------------

.. py:property:: event

   | Provides access to the internal request completion event object.
   | Return type depends on the concurrency mode of the program.
   | In most cases, manual usage of this object is unnecessary.
   |
   | *Disclaimer: Incorrect usage of this object can break things.*

   :raises RuntimeError: on property modification or deletion.

   :return: Reference to the internal event object.
   :rtype: `asyncio.Event`_ in async mode
   :rtype: `threading.Event`_ in sync (threaded) mode


.. py:property:: future

   | Provides access to the internal future-like request object.
   | Return type depends on the concurrency mode of the program.
   | In most cases, manual usage of this object is unnecessary.
   |
   | *Disclaimer: Incorrect usage of this object can break things.*

   :raises RuntimeError: on property modification or deletion.

   :return: Reference to the internal future-like object.
   :rtype: `asyncio.Task`_ in async mode
   :rtype: `concurrent.futures.Future`_ in sync (threaded) mode


.. _threading.Event: https://docs.python.org/3/library/threading.html#threading.Event

.. _asyncio.Event: https://docs.python.org/3/library/asyncio-sync.html#asyncio.Event

.. _asyncio.Task: https://docs.python.org/3/library/asyncio-task.html#asyncio.Task

.. _concurrent.futures.Future: https://docs.python.org/3/library/concurrent.futures.html?highlight=concurrent%20futures%20future#concurrent.futures.Future
