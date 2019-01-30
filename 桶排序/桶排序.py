# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/12/10

def bucket_sort(li, n=100, max_num=10000):
    """
    桶排序
    :param li: 列表
    :param n: 桶的数目
    :param max_num: 数的范围
    :return:
    """
    buckets = [[] for _ in range(n)]  # 创建n个空桶[]，每个桶可以放max_num//n个数的范围
    for var in li:
        i = min(var // (max_num//n),n-1)  # i:var被放到几号桶
        buckets[i].append(var)  # 把var加到桶里
        # 保持桶内的顺序
        for j in range(len(buckets[i])-1,0,-1):  # 倒过来进行桶内排序
            if buckets[i][j]< buckets[i][j-1]:  # 与新加进来的数进行比较
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1],buckets[i][j]
            else:
                break
    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc)
    return sorted_li

import random

li = [random.randint(0, 100) for i in range(10000)]
li = bucket_sort(li)
print(li)
