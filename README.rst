.. image:: https://img.shields.io/badge/License-GPL%20v3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. image:: https://badge.fury.io/py/storage-cache.svg
   :target: https://pypi.org/project/storage-cache/

.. image:: https://img.shields.io/travis/HenleyKuang/storage-cache.svg
   :target: https://travis-ci.org/HenleyKuang/storage-cache


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
