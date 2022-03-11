from yfrake.openapi.generator import generate_openapi_spec
from yfrake.openapi.utils import get_openapi_datatype


def test_openapi_spec_generation():
    generate_openapi_spec()


def test_datatype_matching():
    result = get_openapi_datatype(str)
    assert result == 'string'
    result = get_openapi_datatype(str())
    assert result == 'string'

    result = get_openapi_datatype(int)
    assert result == 'integer'
    result = get_openapi_datatype(int())
    assert result == 'integer'

    result = get_openapi_datatype(bool)
    assert result == 'boolean'
    result = get_openapi_datatype(bool())
    assert result == 'boolean'

    result = get_openapi_datatype(list)
    assert result == 'array'
    result = get_openapi_datatype(list())
    assert result == 'array'

    result = get_openapi_datatype(dict)
    assert result == 'object'
    result = get_openapi_datatype(dict())
    assert result == 'object'

    result = get_openapi_datatype(float)
    assert result == 'number'
    result = get_openapi_datatype(float())
    assert result == 'number'
