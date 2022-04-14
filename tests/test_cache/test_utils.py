from yfrake.cache import utils, const
import time


def test_request_key_digest_size():
    digest = utils.get_request_key('', dict())
    assert digest.__sizeof__() == const.BYTES_OVERHEAD_PARTS['request_key_size']


def test_compare_digests():
    digest_1 = utils.get_request_key('', dict())
    for i in range(0, 100):
        digest_2 = utils.get_request_key(str(i), dict())
        chars_similar = 0
        for count, char in enumerate(digest_1):
            if digest_2[count] == char:
                chars_similar += 1
        assert chars_similar < len(digest_1) / 4


def test_entry_size():
    response = 'qwerty'
    assert len(response) < utils.get_entry_size(response)


def test_exp_date():
    date = utils.get_expiration_date(0.1)
    assert isinstance(date, str)
    time.sleep(0.01)
    assert not utils.is_expired(date)
    time.sleep(0.1)
    assert utils.is_expired(date)


def test_megs_to_bytes():
    assert utils.megs_to_bytes(1) == 1000000
