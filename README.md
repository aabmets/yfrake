# YFrake

<a target="new" href="https://pypi.python.org/pypi/yfrake"><img border=0 src="https://img.shields.io/badge/python-3.10+-blue.svg?label=python" alt="Supported Python versions"></a>
<a target="new" href="https://pypi.python.org/pypi/yfrake"><img border=0 src="https://img.shields.io/pypi/v/yfrake?label=version" alt="Package version on PyPI"></a>
<a target="new" href="https://www.codefactor.io/repository/github/aspenforest/yfrake"><img border=0 src="https://img.shields.io/codefactor/grade/github/aspenforest/yfrake?label=code quality" alt="CodeFactor code quality"></a>
<a target="new" href="https://scrutinizer-ci.com/g/aspenforest/yfrake/"><img border=0 src="https://img.shields.io/scrutinizer/build/g/aspenforest/yfrake" alt="Scrutinizer build inspection"></a>
<a target="new" href="https://app.codecov.io/gh/aspenforest/yfrake"><img border=0 src="https://img.shields.io/codecov/c/github/aspenforest/yfrake" alt="Code coverage"></a> 
<br />
<a target="new" href="https://pypi.python.org/pypi/yfrake"><img border=0 src="https://img.shields.io/pypi/dm/yfrake?label=installs" alt="Installs per month"></a>
<a target="new" href="https://github.com/aspenforest/yfrake/issues"><img border=0 src="https://img.shields.io/github/issues/aspenforest/yfrake" alt="Issues on Github"></a>
<a target="new" href="https://github.com/aspenforest/yfrake/blob/main/LICENSE"><img border=0 src="https://img.shields.io/github/license/aspenforest/yfrake" alt="License on GitHub"></a>
<a target="new" href="https://github.com/aspenforest/yfrake/stargazers"><img border=0 src="https://img.shields.io/github/stars/aspenforest/yfrake?style=social" alt="Stars on GitHub"></a>
<a target="new" href="https://twitter.com/aabmets"><img border=0 src="https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2Faabmets&label=Say%20Thanks" alt="Say thanks on Twitter"></a>


### Description
YFrake is a fast and flexible stock market data scraper and server [&#91;note1&#93;](#footnote1).
It enables developers to ***build powerful apps*** without having to worry about the details of session management or maximizing throughput [&#91;note2&#93;](#footnote2).
YFrake can be used as a client to directly return market data to the current program or 
as a ***programmatically controllable server*** to provide market data to other applications.
In addition, all network requests by the client in ***both*** sync and async modes are ***non-blocking***, 
which means that your program can continue executing your code while network requests are in progress.
The best part about YFrake is its ***built-in swagger API documentation*** which you can use to 
perform test queries and examine the returned responses straight in your web browser.
YFrake is built upon the widely used ***aiohttp*** package and its plugins.

### Documentation

The tutorials and the reference manual is available at: &nbsp; <a target="new" href="http://yfrake.readthedocs.io">yfrake.readthedocs.io</a>

<br />
<a id="footnote1"><sup>&#91;note1&#93;:</sup></a> Stock market data is sourced from Yahoo Finance. 
<br/>
<a id="footnote2"><sup>&#91;note2&#93;:</sup></a> The limits of YFrake are configurable and depend on the capabilities of your system.
<br/>
