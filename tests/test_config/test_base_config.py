from yfrake import config
import pytest


def test_base_config_limit():
    limit = config.limit
    assert isinstance(limit, int)
    with pytest.raises(TypeError):
        config.limit = 'asdfg'
    with pytest.raises(TypeError):
        del config.limit


def test_base_config_timeout():
    timeout = config.timeout
    assert isinstance(timeout, int)
    with pytest.raises(TypeError):
        config.timeout = 'asdfg'
    with pytest.raises(TypeError):
        del config.timeout


def test_base_config_host():
    host = config.host
    assert isinstance(host, str)
    with pytest.raises(TypeError):
        config.host = 'asdfg'
    with pytest.raises(TypeError):
        del config.host


def test_base_config_port():
    port = config.port
    assert isinstance(port, int)
    with pytest.raises(TypeError):
        config.port = 'asdfg'
    with pytest.raises(TypeError):
        del config.port


def test_base_config_backlog():
    backlog = config.backlog
    assert isinstance(backlog, int)
    with pytest.raises(TypeError):
        config.backlog = 'asdfg'
    with pytest.raises(TypeError):
        del config.backlog


def test_base_config_cache_size_mb():
    cache_size_mb = config.cache_size_mb
    assert isinstance(cache_size_mb, int)
    with pytest.raises(TypeError):
        config.cache_size_mb = 'asdfg'
    with pytest.raises(TypeError):
        del config.cache_size_mb


def test_base_config_cache_ttl():
    cache_ttl = config.cache_ttl
    assert isinstance(cache_ttl, dict)
    with pytest.raises(TypeError):
        config.cache_ttl = 'asdfg'
    with pytest.raises(TypeError):
        del config.cache_ttl
