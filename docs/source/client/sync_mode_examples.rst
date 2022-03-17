Sync mode examples
==================


The following example loops at line 7 until an error or a result has arrived:

.. code-block:: python
   :emphasize-lines: 7
   :linenos:

   from yfrake import client

   @client.configure()
   def main()
      resp = client.get('quote_type', symbol='msft')

      while not resp.available():
         # do other stuff

      print(resp.endpoint)
      if not resp.error:
         print(resp.data)

   if __name__ == '__main__':
      main()


The following example blocks at line 7 until an error or a result has arrived:

.. code-block:: python
   :emphasize-lines: 7
   :linenos:

   from yfrake import client

   @client.configure()
   def main()
      resp = client.get('quote_type', symbol='msft')

      resp.wait_for_result()

      print(resp.endpoint)
      if not resp.error:
         print(resp.data)

   if __name__ == '__main__':
      main()


| The following example will fetch all queries in the ``queries`` list concurrently,
| using custom ``limit`` and ``timeout`` configuration settings:

.. code-block:: python
   :emphasize-lines: 20
   :linenos:

   from yfrake import client

   @client.configure(limit=256, timeout=1)
   def main()
      queries = [
         dict(endpoint='quote_type', symbol='msft'),
         dict(endpoint='price_overview', symbol='aapl'),
         dict(endpoint='key_stats', symbol='tsla')
      ]

      results = client.gather(queries)
      while in_progress:
         # do other stuff

      for resp in results:
         print(resp.endpoint)
         if not resp.error:
            print(resp.data)

   if __name__ == '__main__':
       main()

| **Note:** In the case of the example above, to prevent race conditions or exceptions, do **not** modify
| the ``in_progress`` nor the ``results`` collections while client requests are still in progress.
