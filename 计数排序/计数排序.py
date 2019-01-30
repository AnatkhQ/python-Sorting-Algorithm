# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/12/10

def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count+1)]
    print('func_count',count)
    for val in li:
        count[val] += 1  # 给对应位置计数+1
    li.clear()  # 清空原来列表，防止浪费空间复杂度
    for ind,val in enumerate(count):
        for i in range(val):  # 循环每个元素的个数
            li.append(ind)  # 重新把数据写回原列表

import random

li = [random.randint(0,100) for _ in range(1000)]
print('first',li)
count_sort(li)
print('final',li)

"""
时间复杂度：O(n)，虽然有多个for循环，但是和n，即len(li)没有关系，只有第一个循环与n有关系，所以为O(n)
计数排序速度比任何排序都快，但是使用计数排序有前提：
必须知道列表的范围，数字大的也不行，因为如果只有五个数，每个数很大，则要开辟很大的空间
"""