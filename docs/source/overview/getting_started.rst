Getting Started
===============

**How to install the package:**

.. code-block:: python

   pip install yfrake

**How to import the client singleton:**

.. code-block:: python

   from yfrake import client

**How to import the server singleton:**

.. code-block:: python

   from yfrake import server


Both the ``client`` and ``server`` singletons are instances of the corresponding internal ``Client`` and ``Server`` classes.
All public methods of these objects are **classmethods**, so there is no need to instantiate more client or server objects.
The classes have been instantiated internally beforehand to provide the user with lower-case object identifiers.
