# YFrake

<a target="new" href="https://pypi.python.org/pypi/yfrake"><img border=0 src="https://img.shields.io/badge/python-3.7+-blue.svg?label=python" alt="Supported Python versions"></a>
<a target="new" href="https://pypi.python.org/pypi/yfrake"><img border=0 src="https://img.shields.io/pypi/v/yfrake?label=version" alt="Package version on PyPI"></a>
<a target="new" href="https://pypi.python.org/pypi/yfrake"><img border=0 src="https://img.shields.io/pypi/dm/yfrake?label=installs" alt="Installs per month"></a>
<a target="new" href="https://www.codefactor.io/repository/github/aspenforest/yfrake"><img border=0 src="https://img.shields.io/codefactor/grade/github/aspenforest/yfrake?label=code quality" alt="CodeFactor code quality"></a>
<a target="new" href="https://scrutinizer-ci.com/g/aspenforest/yfrake/"><img border=0 src="https://img.shields.io/scrutinizer/build/g/aspenforest/yfrake" alt="Scrutinizer build inspection"></a>
<a target="new" href="https://github.com/aspenforest/yfrake/issues"><img border=0 src="https://img.shields.io/github/issues/aspenforest/yfrake" alt="Issues on Github"></a>
<a target="new" href="https://github.com/aspenforest/yfrake/blob/main/LICENSE"><img border=0 src="https://img.shields.io/github/license/aspenforest/yfrake" alt="License on GitHub"></a>
<a target="new" href="https://github.com/aspenforest/yfrake/stargazers"><img border=0 src="https://img.shields.io/github/stars/aspenforest/yfrake?style=social" alt="Stars on GitHub"></a>

### Description
YFrake is a ***flexible*** and ***agile*** stock market data scraper and server [&#91;note1&#93;](#footnote1).
It enables developers to build powerful apps without having to worry about maximizing network request throughput [&#91;note2&#93;](#footnote1).
YFrake can be used as a client to directly return market data or as a ***programmatically controllable server*** to forward data to web clients.
In addition, all network requests by YFrake are ***non-blocking***, which means that your program can continue running your code while network requests are in progress.
The best part about YFrake is its ***built-in swagger API documentation*** which you can use to perform test queries and examine the returned responses.


### Getting Started
#### Installation
~~~
pip install yfrake
~~~
#### How to import
~~~
from yfrake import tclient  # An instance of ThreadClient class.
from yfrake import aclient  # An instance of AsyncClient class.
from yfrake import server   # An instance of Server class.
~~~
#### ThreadClient example
~~~
tclient.request('historical_prices', symbol='msft', interval='1d', range='1y')
while tclient.is_busy():
    # Do other stuff
if tclient.is_done() and not tclient.response.error:
    print(tclient.response.data)
~~~
#### AsyncClient example
~~~
async def main():
    resp = await aclient.get_historical_prices(symbol='msft', interval='1d', range='1y')
    if not resp.error:
        print(resp.data)
asyncio.run(main())
~~~
#### Server example
~~~
server.start()  # Default address is 'localhost:8888'
# Do some other stuff
server.stop()  # Kills all server sub-processes.
~~~

<br/>
<a id="footnote1"><sup>&#91;note1&#93;:</sup></a> Stock market data is sourced from Yahoo Finance. <br/>
<a id="footnote2"><sup>&#91;note2&#93;:</sup></a> You still need to know how to gather coroutines when using asyncio to maximize throughput.
