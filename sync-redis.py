#!/usr/bin/env python
import redis

def migrate_redis():
    src = redis.StrictRedis(host='source_redis_url', password='',port=6379, db=0)
    dst = redis.StrictRedis(host='destination_redis_url', port=6379, db=0)
    for key in src.keys('*'):
        print("Getting key: ", key)
        value = src.get(key)
        print ("Setting key: ", key)
        try:
            dst.set(key, value)
        except redis.exceptions.ResponseError as err:
            print("Failed to set key: {0} - {1}".format(key,err))
            pass
    return

def run():
    migrate_redis()

if __name__ == '__main__':
    run()
