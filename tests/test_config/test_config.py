from yfrake.config import utils
from yfrake import client, config
import pytest
import os


def test_config_1():
    path = config.file
    assert path == utils.get_default_config_path()
    with pytest.raises(TypeError):
        del config.file
    config.file = path


def test_config_2():
    assert config.is_locked() is False

    @client.session
    def main():
        with pytest.raises(RuntimeError):
            config.file = 'asdfg'
        assert config.is_locked() is True
    main()

    assert config.is_locked() is False


def test_config_3():
    assert not config.HERE.exists()
    config.file = config.HERE
    assert config.HERE.exists()

    @client.session
    def main():
        with pytest.raises(RuntimeError):
            config.file = config.HERE
    main()

    assert config.HERE.exists()
    os.remove(config.HERE)
    assert not config.HERE.exists()
