Reference
=========


.. contents:: Contents

.. raw:: html

   <br />
   <hr>


Public Methods
--------------

.. py:classmethod:: is_locked()

   | Helper method which is used to check if the configuration is
   | being used by the ``client.session`` decorator. Any attempt
   | to change the configuration while the session is open will cause
   | a ``RuntimeError`` to be thrown.

   :return: Value of the config lock status.
   :rtype: bool


.. raw:: html

   <br />
   <hr>


Public Properties
-----------------

.. py:property:: file
   :classmethod:

   | The full path to the configuration file which should be used by the client and the server objects.
   | Can be assigned either a ``pathlib.Path`` or a ``str`` object.

   :raises TypeError: on attempt to delete the property.

   :return: Full path to the config file to be used.
   :rtype: pathlib.Path


.. py:property:: settings
   :classmethod:

   | Deep copied dictionary of the currently loaded configuration.
   | This property is *READ ONLY.*

   :raises TypeError: on attempt to modify the property.
   :raises TypeError: on attempt to delete the property.

   :rtype: dict
