Response reference
========================


.. py:method:: resp.result()
   :async:

   | Coroutine which yields control to the event loop until the underlying async object
   | has finished and the internal callback method has set the response values.
   |
   | *Attention: For async mode usage only.*

   :return: None


.. py:method:: resp.wait_for_result()

   | Blocks the current thread until the underlying threaded async object
   | has finished and the internal callback method has set the response values.
   |
   | *Attention: For sync mode usage only.*

   :return: None


.. py:method:: resp.available()

   | Returns True if the internal callback method has set the response values.

   :return: Request completion status
   :rtype: bool


.. py:method:: resp.get_async_object()

   | Returns a `concurrent.futures.Future`_ object, if ``client.get`` is called in **sync** mode
   | **or** returns an `asyncio.Task`_ object, if ``client.get`` is called in **async** mode.
   |
   | *Disclaimer: Incorrect usage of an underlying async object can break things.*

   :return: Underlying async object reference
   :rtype: `concurrent.futures.Future`_
   :rtype: `asyncio.Task`_


.. _concurrent.futures.Future: https://docs.python.org/3/library/concurrent.futures.html?highlight=concurrent%20futures%20future#concurrent.futures.Future

.. _asyncio.Task: https://docs.python.org/3/library/asyncio-task.html#asyncio.Task