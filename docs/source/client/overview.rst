Overview
========


.. contents:: Contents

.. raw:: html

   <br />
   <hr>


Client Object
-------------

Methods
+++++++

The ``client`` singleton is the main object which is used to request data from the Yahoo Finance API servers.
It has three methods: the ``get`` method, which is used to make a single request, the ``batch_get`` helper method,
which is used to schedule multiple requests with one call, and the ``get_all`` helper method, which requests data
about a single symbol from all symbol-specific endpoints at once.


Decorators
++++++++++

The ``client`` object has a single decorator named ``session``, which opens a session to the Yahoo Finance API servers and
inspects the concurrency mode of your program to adjust its behaviour accordingly.
This enables YFrake to work in async and sync (threaded) modes out-of-the-box.

A function or a coroutine must be decorated with this decorator before any calls to the ``client`` methods are made.
Calls to the ``client`` methods do not have to take place inside the same function or coroutine which was decorated.

For simplicity's sake, it is recommended to decorate the ``main`` function or coroutine of your program,
so the session is opened on program start and closed when the program ends, but in essence any function
or a coroutine can be used, as long as the before-mentioned considerations are taken into account.

The best practice is to have your program activate the decorator only once, because repeatedly opening and closing the session will kill your performance.

*Note:* On Windows machines, the decorator automatically sets the asyncio event loop policy to
*WindowsSelectorEventLoopPolicy*, because the default *WindowsProactorEventLoopPolicy* does not work correctly.
This automatic selection works only when the decorated coroutine of your program is the ``main`` coroutine,
which gets passed into the ``asyncio.run()`` function.


.. raw:: html

   <br />
   <hr>


ClientResponse Object
---------------------

Instances of this object are returned by the ``client.get`` method.
It handles the request and contains the response from the Yahoo Finance API servers
in three properties: ``endpoint``, ``error`` and ``data``.
The ``endpoint`` is a string, while the ``error`` and ``data`` can be either dictionaries or None.
If the request returned with an error, the ``error`` property is a dictionary and the ``data`` property is None.
If the request returned with data, then the ``data`` property is a dictionary and the ``error`` property is None.
This allows the developer to easily check for response status by writing ``if resp.error is None:``.
It has methods to (a)wait for the response and to check its completion status and also
two properties, ``event`` and ``future``, to access the low-level internals of the ``ClientResponse`` object.


.. raw:: html

   <br />
   <hr>


Async- and ThreadResults Object
-------------------------------

Instances of these objects, which are returned by the ``client.batch_get`` and the ``client.get_all`` methods,
are a list-like containers of ``ClientResponse`` objects with additional functionality attached on top.

There are two kinds of results objects: ``AsyncResults`` and ``ThreadResults``. Which one is returned depends
on the concurrency mode of the program. ``AsyncResults`` is returned when the program is running in
async mode and the ``ThreadResults`` is returned when the program is running in sync (threaded) mode.

The results objects can be used with the ``len()`` and ``list()`` functions and the subscript operator ``[]``.
They have methods to (a)wait for the requests and to check their completion statuses and also
generators to iterate over the ``ClientResponse`` objects in a ``for`` or an ``async for`` loop.
These generators guarantee that the objects which they yield into the ``for`` loop have finished their request to the servers.

You can also loop over a results object with ``for resp in results``, but the returned objects are not guaranteed to be in a finished state,
unless you have specifically (a)waited the results object beforehand.
