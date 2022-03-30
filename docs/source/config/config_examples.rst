Examples
========


.. contents:: Contents

.. raw:: html

   <br />
   <hr>


Correct Usage Examples
----------------------

| No config object usage is required to use the default settings:

.. code-block:: python
   :emphasize-lines: 1
   :linenos:

   from yfrake import client

   @client.session
   def main():
       # do stuff

   main()


| Assigning a custom config file in the **Current Working Directory**.
| If the file doesn't exist, it will be created with the default settings.

.. code-block:: python
   :emphasize-lines: 3
   :linenos:

   from yfrake import client, config

   config.file = config.HERE

   @client.session
   def main():
       # do stuff

   main()


Assigning a custom config file in the specified path:

.. code-block:: python
   :emphasize-lines: 3
   :linenos:

   from yfrake import client, config

   config.file = "C:/Users/username/Projects/Project Name/yfrake_settings.ini"

   @client.session
   def main():
       # do stuff

   main()


Assigning a custom config file before the server is started:

.. code-block:: python
   :emphasize-lines: 3
   :linenos:

   from yfrake import server, config

   config.file = Path("C:/Users/username/Projects/Project Name/yfrake_settings.ini")
   server.start()

   # defined behaviour

   server.stop()


.. raw:: html

   <br />
   <hr>


Incorrect Usage Examples
------------------------

Trying to assign a custom config file in the **Current Working Directory**.

.. code-block:: python
   :emphasize-lines: 5
   :linenos:

   from yfrake import client, config

   @client.session
   def main():
       config.file = config.HERE

       # will raise an exception

   main()


Trying to assign a custom custom config file in the specified path:

.. code-block:: python
   :emphasize-lines: 5
   :linenos:

   from yfrake import client, config

   @client.session
   def main():
       config.file = "C:/Users/username/Projects/Project Name/yfrake_settings.ini"

       # will raise an exception

   main()


Assigning a custom config file after the server has started:

.. code-block:: python
   :emphasize-lines: 4
   :linenos:

   from yfrake import server, config

   server.start()
   config.file = Path("C:/Users/username/Projects/Project Name/yfrake_settings.ini")

   # undefined behaviour

   server.stop()
