# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/11/20
import time
import functools

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


@cal_time
def binary_search(li, val):
    """
    :param li:传入列表
    :param val: 需要查找的值
    :return: val
    """
    low = 0  # 指针low：起始最小长度为0
    high = len(li) - 1  # 指针high：最大长度为列表长度-1
    while low <= high:  # 指针low<=high时能够找到值
        mid = (low + high) // 2  # 找到中间值
        if li[mid] > val:  # 二分出来的值与待查找的值进行比较
            high = mid - 1  # high指针移动到mid处-1的位置，即mid左边一位
        elif li[mid] < val:
            low = mid + 1  # low指针移动到mid处+1的位置，即mid右边一位
        else:  # val=mid
            return mid  #拿到找到的值
    else:  # 指针low>high时
        return None  # 列表没有需要查找的值


@cal_time
def linear_search(li, val):
    try:
        return li.index(val)
    except:
        return None

# li = list(range(0,10000,2))  # None找不到偶数
li = list(range(0,100000))
print(binary_search(li,9999))
print(linear_search(li,9999))