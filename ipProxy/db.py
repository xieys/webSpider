# -*- coding: utf-8 -*-

import redis
import random

REDIS_HOST = 'localhost'
REDIS_PORT = '6379'
REDIS_PASSWORD = None
REDIS_KEY = "proxyes"
INIT_SCORE = 10
MAX_SCORE = 100


class Redis(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        """
        初始化连接数据库
        :param host: 地址
        :param port: 端口
        :param password: 密码
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password)

    def add(self, proxy):
        """
        添加代理，并初始化分值
        :param proxy: 代理
        :return:
        """
        self.db.zadd(REDIS_KEY, INIT_SCORE, proxy)

    def set_max_score(self, proxy):
        """
        将代理分数设置为最高分
        :param proxy:代理
        :return:
        """
        self.db.zadd(REDIS_KEY, MAX_SCORE, proxy)

    def reduce_score(self, proxy):
        """
        将代理的分数减1
        :param proxy:代理
        :return:
        """
        self.db.zincrby(REDIS_KEY, -1, proxy)

    def get_single_proxy(self):
        """
        随机返回单个代理
        :return:
        """
        proxyes = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
        if len(proxyes):
            return random.choice(proxyes)
        else:
            proxyes = self.db.zrangebyscore(REDIS_KEY, 0, 100)
            if len(proxyes):
                return random.choice(proxyes)
            else:
                print("代理池枯竭")
                # raise Exception("代理池枯竭")

    def get_all_proxyes(self):
        """
        返回全部代理
        :return:
        """
        return self.db.zrangebyscore(REDIS_KEY, 0, MAX_SCORE)

    def count(self):
        """
        返回代理的总数量
        :return:
        """
        return self.db.zcard(REDIS_KEY)

    def get_proxyes(self, start, stop):
        """
        返回多个代理
        :param start:
        :param stop:
        :return:
        """
        return self.db.zrevrange(REDIS_KEY, start, stop)

    def remove_proxy(self, proxy):
        """
        移除代理
        :param proxy:
        :return:
        """
        self.db.zrem(REDIS_KEY, proxy)

    def is_exist(self, proxy):
        """
        判断代理是否存在数据库中
        :param proxy:
        :return:
        """
        return not self.db.zscore(REDIS_KEY, proxy) is None
