Reference
=========

.. py:classmethod:: server.start()

   Starts the YFrake server. Only one server can be active *per process* at any time.

   :raises RuntimeError: if the server is already running.

   :return: None


.. py:classmethod:: server.stop()

   Stops the YFrake server.

   :raises RuntimeError: if the server is already stopped.

   :return: None


.. py:classmethod:: server.is_running()

   Checks if the server is running.

   :return: Server status
   :rtype: bool