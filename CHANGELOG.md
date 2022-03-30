
# Change Log

### Version 2.0.0

* Changed configuration implementation. <br /> 
In version 1, you could pass arguments directly into the @client.configure() decorator and the server.start() method.
In version 2, the configuration can now be accessed or changed ***only*** through the dedicated 'config' singleton, which can be imported the same way as the 'client' and 'server' objects.
Note: it is not necessary to use the 'config' object, if you wish to run YFrake with the default settings.


* Trying to import YFrake with Python version less than 3.10 will throw a RuntimeError exception. <br />
YFrake uses the new feature of defining union types as 'X | Y' (PEP 604), which is only available from Python 3.10 and upwards.


* The YFrake module itself is now directly runnable, which is used to run the server from the command line with: 'python -m yfrake args'.


* Updated the documentation to reflect the changes above.