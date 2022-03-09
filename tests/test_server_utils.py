from yfrake.server import utils
from yfrake.client.base_response import BaseResponse
from multidict import MultiDictProxy, MultiDict


def test_convert_multidict():
    items = [
        ('key_1', 'value_1'),
        ('key_1', 'value_2'),
        ('key_2', 'value_3'),
        ('key_2', 'value_4')
    ]
    m_dict = MultiDictProxy(MultiDict(items))
    result: dict = utils.convert_multidict(m_dict)

    assert 'value_2' not in result.values()
    assert 'value_4' not in result.values()

    assert list(result.keys()).count('key_1') == 1
    assert list(result.keys()).count('key_2') == 1


def test_pretty_json():
    resp = BaseResponse()
    resp = utils.pretty_json(resp)

    assert isinstance(resp, str)
    assert len(resp) != 0
