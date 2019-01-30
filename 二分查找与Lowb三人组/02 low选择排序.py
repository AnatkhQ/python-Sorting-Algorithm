# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/11/20
from 二分查找与Lowb三人组.time_calculate import cal_time

"""
选择排序：遍历列表，找到最小的数，放在首位
"""

@cal_time
def select_sort(li):
    for i in range(len(li)-1):
        # 第i趟：有序区li[0:i] 无序区li[i:n]，第一趟就位i=0的索引值
        min_loc = i  # 当前循环无序区最小的值，第一次为索引0
        for j in range(i+1, len(li)):  # 循环无序区
            if li[min_loc] > li[j]:  # 当前有序区的最大值对比无序区的值
                min_loc = j  # 下标交换
        li[min_loc], li[i] = li[i], li[min_loc]  # 位置进行交换，相当于li[j]与li[i]进行交换
        print(li)



li = [2,5,4,8,7,6,9,1,3]
select_sort(li)
print(li)