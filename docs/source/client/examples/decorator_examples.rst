Decorator Examples
==================

The following examples open a session with the default settings:

.. code-block:: python
   :emphasize-lines: 1
   :linenos:

   @client.configure()
   def main()
      # do some stuff


.. code-block:: python
   :emphasize-lines: 1
   :linenos:

   @client.configure()
   async def main()
      # do some stuff


.. raw:: html

   <br />


The following examples open a session with custom settings:

.. code-block:: python
   :emphasize-lines: 1
   :linenos:

   @client.configure(limit=128, timeout=8)
   def main()
      # do some stuff


.. code-block:: python
   :emphasize-lines: 1
   :linenos:

   @client.configure(limit=128, timeout=8)
   async def main()
      # do some stuff
