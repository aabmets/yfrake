from yfrake.client.validators import validate_and_sanitize
import pytest


def test_pass():
    args = dict(
        symbol='msft',
        startDate=1000,
        endDate=2000,
        events=True,
        extHours=False
    )
    validate_and_sanitize('historical_prices', args)


def test_invalid_param():
    args = dict(
        symbol='msft',
        startDate=1000,
        endDate=2000,
        events=True,
        extHours=False,
        INVALID_KEY=bool()
    )
    with pytest.raises(KeyError):
        validate_and_sanitize('historical_prices', args)


def test_invalid_datatype():
    args = dict(
        symbol='msft',
        startDate=1000,
        endDate=2000,
        events=True,
        extHours=dict()  # invalid datatype
    )
    with pytest.raises(TypeError):
        validate_and_sanitize('historical_prices', args)
