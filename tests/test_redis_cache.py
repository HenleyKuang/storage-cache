"""
:author: Henley Kuang
:since: 2019-06-14
"""
import json
import pytest

from storage_cache.main import StorageCacheFactory
from storage_cache.types import REDIS_STORAGE_CACHE
from storage_cache.excepts import CacheClassDoesNotExistException

PRIMARY_KEYS = ['primary', 'keys', 'test']
SECONDARY_KEYS = ['secondary', 'keys', 'hashfield']
META_DATA = ['meta', 'data', 'value']
META_DATA_STR = json.dumps(META_DATA)

EXPIRATION = 3600 * 24 * 7 * 2  # 2 weeks

HASH_KEY_PREFIX = 'hash:unittest_prefix'
STR_KEY_PREFIX = 'str:unittest_prefix'

StorageCacheClass = StorageCacheFactory.factory(REDIS_STORAGE_CACHE)
storage_cache_hash = StorageCacheClass(redis_host='127.0.0.1',
                                       redis_port=6379,
                                       redis_password='',
                                       redis_db=0,
                                       key_format=HASH_KEY_PREFIX,
                                       )
storage_cache_str = StorageCacheClass(redis_host='127.0.0.1',
                                      redis_port=6379,
                                      redis_password='',
                                      redis_db=0,
                                      key_format=STR_KEY_PREFIX,
                                      )


def test_set_hash_cache():
    """
    Test return value of setting hash data type
    """
    result = storage_cache_hash.set_cache_hash(
        PRIMARY_KEYS, SECONDARY_KEYS, META_DATA_STR, EXPIRATION)
    result_cmd, result_hash_key_name, result_hash_field_name, result_meta_data_str = result
    result_meta_data = json.loads(result_meta_data_str)
    expected_cmd = 'hset'
    expected_hash_key_name = "%s:%s" % (
        HASH_KEY_PREFIX, ":".join(PRIMARY_KEYS))
    expected_hash_field_name = ":".join(SECONDARY_KEYS)
    expected_meta_data = META_DATA
    assert isinstance(result, tuple)
    assert result_cmd == expected_cmd
    assert result_hash_key_name == expected_hash_key_name
    assert result_hash_field_name == expected_hash_field_name
    assert result_meta_data == expected_meta_data


def test_set_str_cache():
    """
    Test return value of setting str date type
    """
    result = storage_cache_str.set_cache_str(
        PRIMARY_KEYS, META_DATA_STR, EXPIRATION)
    result_cmd, result_str_key_name, result_meta_data_str = result
    result_meta_data = json.loads(result_meta_data_str)
    expected_cmd = 'set'
    expected_str_key_name = "%s:%s" % (STR_KEY_PREFIX, ":".join(PRIMARY_KEYS))
    expected_meta_data = META_DATA
    assert isinstance(result, tuple)
    assert result_cmd == expected_cmd
    assert result_str_key_name == expected_str_key_name
    assert result_meta_data == expected_meta_data


def test_get_hash_cache():
    """
    Test return value of getting hash date type
    """
    result = storage_cache_hash.get_cache_hash(
        PRIMARY_KEYS, SECONDARY_KEYS)
    result_meta_data_str = result
    result_meta_data = json.loads(result_meta_data_str)
    expected_meta_data = META_DATA
    assert isinstance(result, str)
    assert result_meta_data == expected_meta_data


def test_get_str_cache():
    """
    Test return value of getting str data type
    """
    result = storage_cache_str.get_cache_str(
        PRIMARY_KEYS)
    result_meta_data_str = result
    result_meta_data = json.loads(result_meta_data_str)
    expected_meta_data = META_DATA
    assert isinstance(result, str)
    assert result_meta_data == expected_meta_data
