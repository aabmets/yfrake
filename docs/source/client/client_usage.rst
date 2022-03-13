How to use the client
=====================

This page describers installation guide.

.. code-block:: python
   :caption: Example:
   :emphasize-lines: 5
   :linenos:

   from yfrake import client

   @client.configure(limit=100, timeout=1)
   def main()
     resp = client.get('quote_type', symbol='msft')

     while not resp.available():
         # do other stuff

     if not resp.error:
         print(resp.endpoint)
         print(resp.data)

   if __name__ == '__main__':
     main()