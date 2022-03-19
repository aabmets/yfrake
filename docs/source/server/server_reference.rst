Reference
=========

.. py:classmethod:: server.start(host='localhost', port=8888, limit=64, timeout=2, backlog=128)

   Starts the YFrake server. Only one server can be active *per process* at any time.

   :param host: The web address of the host.
   :type host: str

   :param port: The port number of the host.
   :type port: int

   :param limit: The maximum number of concurrent requests opened to the Yahoo Finance servers.
   :type limit: int

   :param timeout: Maximum allowed time per request to fetch data from the Yahoo Finance servers, in seconds.
   :type timeout: int

   :param backlog: A number of unaccepted connections that the system will allow before refusing new connections.
   :type backlog: int

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