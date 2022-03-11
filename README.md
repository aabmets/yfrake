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




### Disclaimer
The current version of YFrake is usable, but ***not*** production ready.

### Description
YFrake is a ***flexible*** and ***agile*** stock market data scraper and server [&#91;note1&#93;](#footnote1).
It enables developers to build powerful apps without having to worry about maximizing network request throughput [&#91;note2&#93;](#footnote1).
YFrake can be used as a client to directly return market data or as a ***programmatically controllable server*** to forward data to web clients.
In addition, all network requests by YFrake are ***non-blocking***, which means that your program can continue running your code while network requests are in progress.
The best part about YFrake is its ***built-in swagger API documentation*** which you can use to perform test queries and examine the returned responses.


### Getting started
How to install yfrake:
~~~
pip install yfrake
~~~
How to import yfrake:
~~~
from yfrake import client, server
~~~

### Server examples
How to run the server with default settings:
~~~
server.start()
# do other stuff
server.stop()
~~~
How to run the server with custom settings:
~~~
settings = dict(
    host='localhost',
    port=8888,
    limit=100,
    timeout=1,
    backlog=200
)
server.start(**settings)
# do other stuff
server.stop()
~~~


### Sync execution examples
How to continue the current function while checking for response status:
~~~
from yfrake import client

@client.configure(limit=100, timeout=1)
def main()
    resp = client.get('quote_type', symbol='msft')
    
    while not resp.available():
        # do other stuff
        
    if not resp.error:
        print(resp.endpoint)
        print(resp.data)
    
if __name__ == '__main__':
    main()
~~~
How to pause the current function to wait for the result:
~~~
from yfrake import client

@client.configure(limit=100, timeout=1)
def main()
    resp = client.get('quote_type', symbol='msft')
    
    resp.wait_for_result()
    
    if not resp.error:
        print(resp.endpoint)
        print(resp.data)
    
if __name__ == '__main__':
    main()
~~~
How to run multiple queries concurrently:
~~~
from yfrake import client
import time

@client.configure(limit=100, timeout=1)
def main()
    def save_result(obj):
        resp = in_progress.pop(obj)
        resp.wait_for_result()
        results.append(resp)

    in_progress = dict()
    results = list()
    args_list = [
        dict(endpoint='quote_type', symbol='msft'),
        dict(endpoint='price_overview', symbol='aapl')
    ]
    for args_dict in args_list:
        resp = client.get(**args_dict)
        obj = resp.get_async_object()
        obj.add_done_callback(save_result)
        in_progress[obj] = resp

    while in_progress:
        time.sleep(0)
    for resp in results:
        if not resp.error:
            print(resp.endpoint)
            print(resp.data)
    
if __name__ == '__main__':
    main()
~~~

### Async execution examples
How to continue the current coroutine while checking for response status:
~~~
from yfrake import client
import asyncio

@client.configure(limit=100, timeout=1)
async def main():
    resp = client.get('quote_type', symbol='msft')
    
    while not resp.available():
        # do other stuff
        
    if not resp.error:
        print(resp.endpoint)
        print(resp.data)

if __name__ == '__main__':
    asyncio.run(main())
~~~
How to pause the current coroutine to await for the result:
~~~
from yfrake import client
import asyncio

@client.configure(limit=100, timeout=1)
async def main():
    resp = client.get('quote_type', symbol='msft')
    
    await resp.result()
    
    if not resp.error:
        print(resp.endpoint)
        print(resp.data)

if __name__ == '__main__':
    asyncio.run(main())
~~~
How to run multiple queries concurrently:
~~~
from yfrake import client
import asyncio

@client.configure(limit=100, timeout=1)
async def main():
    args_list = [
        dict(endpoint='quote_type', symbol='msft'),
        dict(endpoint='price_overview', symbol='aapl')
    ]
    tasks_list = []
    for args_dict in args_list:
        resp = client.get(**args_dict)
        obj = resp.get_async_object()
        tasks_list.append(obj)

    results = await asyncio.gather(*tasks_list)
    for resp in results:
        if not resp.error:
            print(resp.endpoint)
            print(resp.data)

if __name__ == '__main__':
    asyncio.run(main())
~~~

<br/>
<a id="footnote1"><sup>&#91;note1&#93;:</sup></a> Stock market data is sourced from Yahoo Finance. <br/>
<a id="footnote2"><sup>&#91;note2&#93;:</sup></a> You still need to know how to correctly use asyncio.
