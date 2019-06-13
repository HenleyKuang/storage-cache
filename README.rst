Cloud Storage Cache
===================

Installation
------------

.. code-block:: bash

    pip install cloud-storage-cache


How to use
----------

.. code-block:: python

    from cloud_storage_cache import CloudStorageCacheFactory
    from cloud_storage_cache.types import REDIS_STORAGE_CACHE

    CloudStorageCache = CloudStorageCacheFactory.factory(REDIS_STORAGE_CACHE)
    cloud_storage_cache = CloudStorageCache(
        <redis_host>, <redis_port>, <redis_password>, <redis_db>, <key_format>)
