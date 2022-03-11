from yfrake.client import validator
import pytest

tests = [
    (
        {
            "endpoint": {
                "result": [
                    {"key": "value"}
                ],
                "error": False
            }
        },
        True
    ), (
        {
            "endpoint": {
                "result": [
                    {}
                ],
                "error": False
            }
        },
        False
    ), (
        {
            "endpoint": {
                "result": [],
                "error": False
            }
        },
        False
    ), (
        {
            "endpoint": {
                "result": [
                    {"key": "value"}
                ],
                "error": True
            }
        },
        False
    ), (
        {
            "endpoint": {
                "result": [{}],
                "error": True
            }
        },
        False
    ), (
        {
            "endpoint": {
                "result": [],
                "error": True
            }
        },
        False
    ), (
        {
            "key": "value",
            "news": [
                {"key": "value"}
            ]
        },
        True
    )
]


@pytest.mark.parametrize('arg,result', tests)
async def test_validate(arg, result):
    assert await validator.validate_response(arg) is result
