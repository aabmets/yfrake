Examples
========


Running the server programmatically:

.. code-block:: python
   :emphasize-lines: 4
   :linenos:

   from yfrake import server

   if not server.is_running()
       server.start()

   # do other stuff

   if server.is_running()
       server.stop()

|
| Creating the 'yfrake_settings.ini' file to the *CWD* if it doesn't exist, without running the server:
| ``$ python -m yfrake --config-file here``
|
|
| **Running the server from the terminal:**

| 1) With the default configuration:
| ``$ python -m yfrake --run-server``

| 2) With 'yfrake_settings.ini' in the *CWD*:
| ``$ python -m yfrake --run-server --config-file here``

| 3) With the config file in a custom directory:
| ``$ python -m yfrake --run-server --config-file "/path/to/'yfrake_settings.ini"``


