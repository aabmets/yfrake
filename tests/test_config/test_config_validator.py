from yfrake import config
from pathlib import Path
import pytest


configs_dir = Path(__file__).with_name('config_files')


def test_good_config():
    file = configs_dir.joinpath('good_config.ini')
    try:
        config.file = file
    except (AttributeError, KeyError, ValueError):
        pytest.fail('Good config raised an exception.')


def test_missing_section():
    file = configs_dir.joinpath('missing_section.ini')
    with pytest.raises(AttributeError):
        config.file = file


def test_missing_field():
    file = configs_dir.joinpath('missing_field.ini')
    print(file)
    with pytest.raises(KeyError):
        config.file = file


def test_bad_field_type():
    file = configs_dir.joinpath('bad_field_type.ini')
    with pytest.raises(ValueError):
        config.file = file
