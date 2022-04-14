from yfrake.cache import cache, utils
import time
import json


cache = cache.CacheSingleton()

ttl_groups = getattr(cache, 'ttl_groups')
ttl_short = getattr(cache, 'ttl_short')
ttl_short['options'] = 0.1


def test_ttl_groups_override():
    ttl_groups['override'] = True
    ttl = cache.get_ttl_value('options')
    date = utils.get_expiration_date(ttl)
    assert utils.is_expired(date)

    ttl_groups['override'] = False
    ttl = cache.get_ttl_value('options')
    date = utils.get_expiration_date(ttl)
    assert not utils.is_expired(date)


def test_expiration_date():
    ttl = cache.get_ttl_value('options')
    date = utils.get_expiration_date(ttl)
    assert not utils.is_expired(date)
    time.sleep(0.2)
    assert utils.is_expired(date)


def test_cache_size():
    response = dict(key='value')
    cache.set('options', dict(), response)
    entry_size = utils.get_entry_size(json.dumps(response))

    assert len(cache.cache) == 1
    assert cache.mem_in_use == entry_size
    cache.remove_entry()
    assert len(cache.cache) == 0
    assert cache.mem_in_use == 0
    del cache.mem_in_use


def test_is_memory_full():
    size = 64000001
    assert cache.is_space_full(size) is True


def test_is_cache_full():
    cache.max_entries = 1
    cache.cache['key'] = 'value'
    assert cache.is_space_full(0)
    del cache.cache['key']
    assert not cache.is_space_full(0)


def test_is_entry_size_valid():
    assert cache.is_entry_size_valid(999999) is True
    assert cache.is_entry_size_valid(1000000) is False


def test_cache_main():
    endpoint = 'options'
    params = dict(symbol='MSFT')

    response = cache.get(endpoint, params)
    assert response is None

    cache.set(endpoint, params, dict(key='value'))

    response = cache.get(endpoint, params)
    assert response.get('key') == 'value'

    time.sleep(0.2)

    response = cache.get(endpoint, params)
    assert response is None


def test_cache_lru():
    cache.max_entries = 3
    endpoints = [
        'insights',
        'financials',
        'news',
        'trending_symbols'
    ]
    params = {'symbol': 'MSFT'}
    response = {'key': 'value'}

    keys = list()
    for endpoint in endpoints:
        query = dict(
            endpoint=endpoint,
            params=params
        )
        key = utils.get_request_key(**query)
        keys.append(key)
        query['response'] = response
        cache.set(**query)

    assert list(cache.cache.keys()) == [keys[3], keys[2], keys[1]]
    cache.get(endpoints[1], params)
    assert list(cache.cache.keys()) == [keys[1], keys[3], keys[2]]
    cache.get(endpoints[2], params)
    assert list(cache.cache.keys()) == [keys[2], keys[1], keys[3]]
    cache.set(endpoints[0], params, response)
    assert list(cache.cache.keys()) == [keys[0], keys[2], keys[1]]
