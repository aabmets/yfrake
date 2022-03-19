Sync (Threaded) Mode Examples
=============================


.. contents:: Contents

.. raw:: html

   <br />
   <hr>


Client.get() Examples
---------------------

The following example loops at line 4 ``while`` the response has not yet arrived:

.. code-block:: python
   :emphasize-lines: 4
   :linenos:

   @client.configure()
   def main():
      resp = client.get('quote_type', symbol='msft')
      while resp.pending():
         # do some other stuff


The following example blocks at line 4 until the response has arrived:

.. code-block:: python
   :emphasize-lines: 4
   :linenos:

   @client.configure()
   def main():
      resp = client.get('quote_type', symbol='msft')
      resp.wait()
      # do some other stuff


.. raw:: html

   <br />
   <hr>


Client.batch_get() Examples
---------------------------

The following example waits until all of the responses have arrived before running the ``for`` loop:

.. code-block:: python
   :emphasize-lines: 9
   :linenos:

   @client.configure()
   def main():
      queries = [
         dict(endpoint='quote_type', symbol='msft'),
         dict(endpoint='price_overview', symbol='aapl'),
         dict(endpoint='key_statistics', symbol='tsla')
      ]
      results = client.batch_get(queries)
      for resp in results.gather():
         # do some stuff with the resp


The following example starts yielding the responses into the ``for`` loop as soon as they become available:

.. code-block:: python
   :emphasize-lines: 9
   :linenos:

   @client.configure()
   def main():
      queries = [
         dict(endpoint='quote_type', symbol='msft'),
         dict(endpoint='price_overview', symbol='aapl'),
         dict(endpoint='key_statistics', symbol='tsla')
      ]
      results = client.batch_get(queries)
      for resp in results.as_completed():
         # do some stuff with the resp


.. raw:: html

   <br />
   <hr>


Client.get_all() Examples
---------------------------

The following example loops while all the available data about a symbol is being retrieved:

.. code-block:: python
   :emphasize-lines: 4
   :linenos:

   @client.configure()
   def main():
      results = client.get_all(symbol='msft')
      while results.pending():
         # do some other stuff


The following example blocks while all the available data about a symbol is being retrieved:

.. code-block:: python
   :emphasize-lines: 4
   :linenos:

   @client.configure()
   def main():
      results = client.get_all(symbol='aapl')
      results.wait()
      # do some other stuff

**WARNING:** A single call to ``get_all()`` creates 32 simultaneous network requests and
can return up to 1.5 megabytes of data, so uncontrolled usage of this method
*may* deplete the memory of your system and *may* get your IP blacklisted by Yahoo.
