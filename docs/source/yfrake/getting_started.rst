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


The ``client``, ``server``, and ``config`` objects are singletons,
which have been instantiated internally beforehand to provide the user with lower-case object name identifiers.

**NB!** The minimum required Python version for YFrake is **Python 3.10**.
From YFrake version **2.0.0** forward, trying to import YFrake in lower Python versions will raise a **RuntimeError**.