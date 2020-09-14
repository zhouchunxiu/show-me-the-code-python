"""
生成200个激活码并存入Redis
"""
import uuid
import redis
from ss0003.configs.redis_conf import config

red = redis.Redis(**config)
# 生成激活码并存入redis
for i in range(200):
    id = str(uuid.uuid1())
    red.set(i, id)
    # print(red.get(i))
