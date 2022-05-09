Overview
========

Configuration settings for YFrake are stored in a file named ``yfrake_settings.ini``.
The ``config`` singleton reads the settings from that file and configures the ``client`` and the ``server`` objects.
It is not necessary to use the ``config`` object, if you want to run YFrake with the default settings.

The config has two properties named ``file`` and ``settings`` and one method named ``is_locked``,
which is used to check if the configuration is **locked**, i.e., the ``client.session`` decorator is in use (active).

All the properties of the ``config`` object can be **read** at any time, but the ``file`` property
can be modified **only** when the ``client.session`` decorator is **not** in use (active).
The ``file`` property can accept either a pathlib.Path or a string object, which contains a full path to a config file.
Modifying the ``file`` property after the ``server`` has started has undefined behaviour and is therefore **not recommended**.

Accessing the ``settings`` property will return a dictionary of the currently loaded configuration.
Modifying this dictionary does not modify the currently loaded configuration.

The ``config`` object also has an attribute named ``HERE``, which points to an abstract config file in the **Current Working Directory**.
Assigning the ``HERE`` attribute to the ``file`` property will create the config file in the **CWD** with the default settings, if it doesn't exist.
