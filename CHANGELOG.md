
# Change Log


### Version 2.1.0

* Implemented caching functionality. Now, all endpoint results are cached using a TLRU algorithm.
The cache behaviour is fully customizable from the configuration file.


* Reworked the config object implementation to support the caching functionality. <br /> 
The config object no longer has separate attributes for each setting, but rather a single "settings" attribute,
from which all currently enabled config settings can be read.


* Added tests for the cache functionality and improved config testing.


* Improved documentation to explain caching and the contents of the configuration file.


* Fixed a server bug which caused the swagger docs to return bad responses for good requests.


### Version 2.0.0

* Changed configuration implementation. <br /> 
In version 1, you could pass arguments directly into the @client.configure() decorator and the server.start() method.
In version 2, the configuration can now be accessed or changed ***only*** through the dedicated 'config' singleton, which can be imported the same way as the 'client' and 'server' objects.
Note: it is not necessary to use the 'config' object, if you wish to run YFrake with the default settings.


* Trying to import YFrake with Python version less than 3.10 will throw a RuntimeError exception. <br />
YFrake uses the new feature of defining union types as 'X | Y' (PEP 604), which is only available from Python 3.10 and upwards.


* The YFrake module itself is now directly runnable, which is used to run the server from the command line with: 'python -m yfrake args'.


* Updated the documentation to reflect the changes above.