ThreadResults Reference
=======================


.. contents:: Contents

.. raw:: html

   <br />
   <hr>


Public Methods
--------------

.. py:method:: pending()
   :noindex:

   Function which checks the completion statuses of all its requests by calling the ``pending()`` method on each ``ClientResponse``.
   Returns ``True`` if at least one request is still in progress.

   :return: Request completion status
   :rtype: bool


.. py:method:: wait()
   :noindex:

   | Waits until all its requests have completed.

   :return: None


.. py:method:: gather()
   :noindex:

   | Synchronous generator which can be used in the ``for`` loop.
   | Waits for and starts yielding results when all requests have completed.

   :return: Request response objects
   :rtype: ClientResponse


.. py:method:: as_completed()
   :noindex:

   | Synchronous generator which can be used in the ``for`` loop.
   | Waits for and starts yielding results immediately as they become available.

   :return: Request response objects
   :rtype: ClientResponse
