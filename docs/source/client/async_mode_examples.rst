Async mode examples
===================


The following example loops at line 8 until an error or a result has arrived:

.. code-block:: python
   :emphasize-lines: 8
   :linenos:

   from yfrake import client
   import asyncio

   @client.configure()
   async def main()
      resp = client.get('quote_type', symbol='msft')

      while not resp.available():
         # do other stuff

      print(resp.endpoint)
      if not resp.error:
         print(resp.data)


   if __name__ == '__main__':
      asyncio.run(main())


The following example blocks at line 8 until an error or a result has arrived:

.. code-block:: python
   :emphasize-lines: 8
   :linenos:

   from yfrake import client
   import asyncio

   @client.configure()
   async def main()
      resp = client.get('quote_type', symbol='msft')

      await resp.result()

      print(resp.endpoint)
      if not resp.error:
         print(resp.data)


   if __name__ == '__main__':
      asyncio.run(main())


| The following example will fetch all queries in the ``queries`` list concurrently,
| using custom ``limit`` and ``timeout`` configuration settings:

.. code-block:: python
   :emphasize-lines: 14
   :linenos:

   from yfrake import client
   import asyncio

   @client.configure(limit=256, timeout=1)
   async def main():
      queries = [
         dict(endpoint='quote_type', symbol='msft'),
         dict(endpoint='price_overview', symbol='aapl'),
         dict(endpoint='key_stats', symbol='tsla')
      ]

      results = await client.collect(queries)

      for resp in results:
         print(resp.endpoint)
         if not resp.error:
            print(resp.data)


   if __name__ == '__main__':
      asyncio.run(main())
