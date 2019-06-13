"""
:author: Henley Kuang
:since: 06/13/2019
"""
from cloud_storage_cache.cache.redis_cache import CloudStorageRedisCache
from cloud_storage_cache.types import REDIS_STORAGE_CACHE
from cloud_storage_cache.excepts import CacheClassDoesNotExistException

CACHE_TYPE_CLASS = {
    REDIS_STORAGE_CACHE: CloudStorageRedisCache,
}


class CloudStorageCacheFactory(object):
    @staticmethod
    def factory(cache_type):
        try:
            return CACHE_TYPE_CLASS[cache_type]
        except KeyError as e:
            raise CacheClassDoesNotExistException(
                "Invalid value passed into CloudStorageCacheFactory: %s" % cache_type)
