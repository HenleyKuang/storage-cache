import argparse
import logging
import json

from storage_cache import StorageCacheFactory
from storage_cache.util.config import DEFAULT_LOG_FORMAT_STRING

LOGGER = logging.getLogger(__name__)


def _parse_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)

    base_parser = argparse.ArgumentParser(add_help=False)
    base_parser.add_argument('--cache-type',  required=True)
    base_parser.add_argument('--redis-host', required=True)
    base_parser.add_argument('--redis-port', required=True)
    base_parser.add_argument('--redis-password')
    base_parser.add_argument('--redis-db', required=True)
    base_parser.add_argument('--key-format', required=True, help='key prefix')
    base_parser.add_argument('--primary-keys', nargs='+',
                             required=True, help='list of strings')

    hash_parser = argparse.ArgumentParser(add_help=False)
    hash_parser.add_argument('--secondary-keys', nargs='+',
                             required=True, help='list of strings')

    set_parser = argparse.ArgumentParser(add_help=False)
    set_parser.add_argument('--meta-data', nargs='+',
                            required=True, help='list of strings')

    command_subparser = parser.add_subparsers(dest='sub_command')
    command_subparser.required = True

    command_subparser.add_parser(
        'set-hash', parents=[base_parser, hash_parser, set_parser])
    command_subparser.add_parser(
        'get-hash', parents=[base_parser, hash_parser])
    command_subparser.add_parser('set-str', parents=[base_parser, set_parser])
    command_subparser.add_parser('get-str', parents=[base_parser])

    return parser.parse_args()


def _main():
    options = _parse_args()
    cache_type = options.cache_type
    redis_host = options.redis_host
    redis_port = options.redis_port
    redis_password = options.redis_password
    redis_db = options.redis_db
    key_format = options.key_format
    primary_keys = options.primary_keys

    StorageCache = StorageCacheFactory.factory(cache_type)

    storage_cache = StorageCache(
        redis_host, redis_port, redis_password, redis_db, key_format)

    expiration_timeout = 3600 * 24 * 7 * 2  # 2 weeks

    if options.sub_command == 'set-hash':
        secondary_keys = options.secondary_keys
        meta_data = json.dumps(options.meta_data)
        result = storage_cache.set_cache_hash(
            primary_keys, secondary_keys, meta_data, expiration_timeout)
    elif options.sub_command == 'get-hash':
        secondary_keys = options.secondary_keys
        result_str = storage_cache.get_cache_hash(
            primary_keys, secondary_keys)
        result = json.loads(result_str)
    elif options.sub_command == 'set-str':
        meta_data = json.dumps(options.meta_data)
        result = storage_cache.set_cache_str(
            primary_keys, meta_data, expiration_timeout)
    elif options.sub_command == 'get-str':
        result_str = storage_cache.get_cache_str(primary_keys)
        result = json.loads(result_str)

    LOGGER.info(result)


if __name__ == '__main__':
    logging.basicConfig(format=DEFAULT_LOG_FORMAT_STRING,
                        datefmt="%Y-%m-%d %H:%M:%S", level=logging.INFO)
    _main()
