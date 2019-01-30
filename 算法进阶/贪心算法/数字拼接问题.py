# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/12/12

""""""
"""
有n个⾮负整数，将其按照字符串拼接的方式拼接为一个整数。
如何拼接可以使得到的整数最大？
例：32,94,128,1286,6,71可以拼接除的最大整数为
94716321286128
"""
from functools import cmp_to_key

li = [32, 94, 128, 1286, 6, 71]


def xy_cmp(x, y):
    """
    函数必须有两个参数用来进行比较
    :param x:
    :param y:
    :return:
    """
    if x + y < y + x:  # x放前面
        print('<', x, y)
        return 1
    elif x + y > y + x:  # y放前面
        print('>',x,y)
        return -1
    else:  # 相同位置排序无所谓
        return 0


def number_join(li):
    li = list(map(str, li))  # 全部转换为str
    li.sort(key=cmp_to_key(xy_cmp))  # cmp_to_key(比较函数)
    return "".join(li)


print(number_join(li))
