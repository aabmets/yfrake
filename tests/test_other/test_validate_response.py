from yfrake.client.validators import validate_response
from yfrake.client.exceptions import BadRequestError
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
            "key": "value",
            "news": [
                {"key": "value"}
            ]
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
    )
]


@pytest.mark.parametrize('arg,result', tests)
async def test_validate_response(arg, result):
    if result is False:
        with pytest.raises(BadRequestError):
            await validate_response(arg)
    else:
        await validate_response(arg)
