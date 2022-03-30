Getting Started
===============

**Install the package by executing:**

.. code-block:: python

   pip install yfrake


**Import the public objects with:**

.. code-block:: python

   from yfrake import client, server, config


.. raw:: html

   <br />


| The ``client``, ``server``, and ``config`` objects are all singletons, which have public **classmethods**.
| The classes have been instantiated internally beforehand to provide the user with lower-case object name identifiers.

You can get the list of valid endpoints and their arguments by running the server and reading the Swagger documentation.
To convert the servers endpoint path param names for use with the client object, just omit the ``/`` character from the
beginning of the endpoint name: ``/company_overview`` becomes ``company_overview``.

**NB!** Trying to import yfrake objects in Python version less than **3.10** will throw an exception!