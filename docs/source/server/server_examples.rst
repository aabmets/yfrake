Examples
========


Running the server programmatically with the default settings:

.. code-block:: python
   :emphasize-lines: 2
   :linenos:

   if not server.is_running()
      server.start()

   # do other stuff

   if server.is_running()
      server.stop()


Running the server programmatically with custom settings:

.. code-block:: python
   :emphasize-lines: 10
   :linenos:

   settings = dict(
      host='localhost',
      port=8888,
      limit=64,
      timeout=2,
      backlog=128
   )

   if not server.is_running()
      server.start(**settings)

   # do other stuff

   if server.is_running()
      server.stop()


Running the server from the command line or terminal:

``$ python "/path/to/python/Lib/site-packages/yfrake/server/runner.py" args``

| It is not necessary to provide any args, if you want to run the server with the default settings.
| The default values for the available args are as follows:

``--host 'localhost'``
``--port 8888``
``--limit 64``
``--timeout 2``
``--backlog 128``
