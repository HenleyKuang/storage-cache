=============
Storage Cache
=============

Installation
------------

.. code-block:: bash

    pip install storage-cache


How to use
----------

.. code-block:: python

    from storage_cache import StorageCacheFactory
    from storage_cache.types import REDIS_STORAGE_CACHE

    StorageCache = StorageCacheFactory.factory(REDIS_STORAGE_CACHE)
    storage_cache = StorageCache(
        <redis_host>, <redis_port>, <redis_password>, <redis_db>, <key_format>)
