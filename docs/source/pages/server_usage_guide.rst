How to use the server
=====================

This page describers installation guide.

.. code-block:: python
   :caption: Example:
   :emphasize-lines: 2
   :linenos:

   server.start()
   # do other stuff
   server.stop()


.. code-block:: python
   :caption: Example:
   :emphasize-lines: 5
   :linenos:

   settings = dict(
     host='localhost',
     port=8888,
     limit=100,
     timeout=1,
     backlog=200
   )
   server.start(**settings)
   # do other stuff
   server.stop()