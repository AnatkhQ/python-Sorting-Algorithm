# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/12/12

""""""
"""
假设商店⽼老老板需要找零n元钱，钱币的⾯面额有：100元、50元、20元、5元、1元，如何找零使得所需钱币的数量量最少？  
"""
t = [100, 50, 20, 5]  # 面值，需要进行排序sort/sorted

def change(t, n):
    """
    找零问题
    :param t: 面值列表
    :param n: 需要零钱
    :return:
    """
    m = [0 for _ in range(len(t))]  # 生成[0,0,0,0]对应每一个面值的个数
    for i, money in enumerate(t):  # 循环面值
        m[i] = n // money  # 面值对应区域 = 从最大面值开始，需要对面值列表进行排序
        n = n % money  # 剩余零钱
    return m, n

print(change(t, 376))