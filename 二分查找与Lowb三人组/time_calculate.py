# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/11/20
import functools,time

def cal_time(func):
    # 装饰器
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("{0} running {1}".format(func.__name__,t2-t1))
        return result
    return wrapper