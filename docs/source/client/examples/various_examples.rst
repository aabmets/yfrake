Various Examples
================


The following example prints out the names of all the endpoints queried:

.. code-block:: python
   :linenos:

   from yfrake import client
   import asyncio

   @client.configure(limit=1024, timeout=1)
   async def main():
      results = client.get_all(symbol='msft')
      async for resp in results.gather():
         print(f'Endpoint: {resp.endpoint}')

   if __name__ == '__main__':
      asyncio.run(main())


The following example prints out either the ``error`` or the ``data`` property of the ``ClientResponse`` objects:

.. code-block:: python
   :linenos:

   from yfrake import client
   import asyncio

   @client.configure(limit=1024, timeout=1)
   async def main():
      queries = [
         dict(endpoint='quote_type', symbol='msft'),
         dict(endpoint='price_overview', symbol='aapl'),
         dict(endpoint='key_statistics', symbol='tsla')
      ]
      results = client.batch_get(queries)
      await results.wait()
      for resp in results:
         if resp.error:
            print(f'Error: {resp.error}')
         else:
            print(f'Data: {resp.data}')

   if __name__ == '__main__':
      asyncio.run(main())


The following example creates a batch request of 3 endpoints for 3 symbols:

.. code-block:: python
   :linenos:

   from yfrake import client

   @client.configure(limit=1024, timeout=1)
   def main():
      all_queries = list()
      for symbol in ['msft', 'aapl', 'tsla']:
         queries = [
            dict(endpoint='quote_type', symbol=symbol),
            dict(endpoint='price_overview', symbol=symbol),
            dict(endpoint='key_statistics', symbol=symbol)
         ]
         all_queries.extend(queries)

      results = client.batch_get(all_queries)
      results.wait()

      count = len(all_queries)
      print(f'ClientResponse objects: {count}')  # 9

   if __name__ == '__main__':
      main()
