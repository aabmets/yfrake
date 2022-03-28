from yfrake.config import config as cfg
import pytest


config = cfg.ConfigSingleton()


def test_config_singleton_1():
    assert isinstance(config, cfg.ConfigSingleton)
    for key in config:
        assert key in ['client', 'server', 'other', 'cache_ttl']
        assert isinstance(config[key], dict)
        with pytest.raises(TypeError):
            config[key] = 'asdfg'
        with pytest.raises(TypeError):
            del config[key]


def test_config_singleton_2():
    path = config.file
    assert path == cfg.get_default_config_path()
    with pytest.raises(TypeError):
        del config.file
    config.file = path
