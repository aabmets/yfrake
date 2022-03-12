from yfrake.client.validators import validate_response
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
async def test_validate_response(arg, result):
    assert await validate_response(arg) is result
