Getting Started
===============

**Install the package by executing:**

``pip install yfrake``


**Import the public objects with:**

.. code-block:: python

   from yfrake import client, server


.. raw:: html

   <br />

Both the ``client`` and ``server`` objects are singletons and instances of the corresponding internal ``Client`` and ``Server`` classes.
All public methods of these objects are **classmethods**, so there is no need to create more client or server objects.
The classes have been instantiated internally beforehand to provide the user with lower-case object name identifiers.

You can get the list of valid endpoints and their arguments by running the server and reading the Swagger documentation.
To convert the servers endpoint path param names for use with the client object, just strip the ``/`` character from the
beginning of the endpoint string: ``/company_overview`` becomes ``company_overview``.
