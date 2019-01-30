# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/11/20
from 二分查找与Lowb三人组.time_calculate import cal_time

"""
插入排序法：
    思路：扑克牌排序
    每次从无序区选择一个元素插入有序区（此方法为相对有序），直至无序区变空
    一共有n张牌，开始有一张，一共模n-1次牌
"""


@cal_time
def insert_sort(li):
    for i in range(1, len(li)):  # i既表示趟数，也表示摸到的牌的下标
        j = i - 1  # j指手里的最后一张牌的下标，第一趟只有一张牌，即列表第一个值，下标为0
        tmp = li[i]  # 在无序区新拿到的值
        print(tmp)
        print(li[j])
        while j >= 0 and li[j] > tmp:  # 当手上的牌还有牌大于新的牌 and 当手上最右边的牌大于新摸到的牌tmp
            # while循环的作用：找插入位置
            li[j + 1] = li[j]  # j指针的位置(手上最右边的牌)向右移一个单位
            j -= 1  # 指针向左移一个单位，找手上从右往左第二个值，再循环进行比较
        li[j + 1] = tmp  # 大于新摸到的牌，全部向右移一个单位，下标j+1(新摸得牌的下标)处为新的数
        print(li)


import random

li = [2, 5, 4, 8, 7, 6, 9, 1, 3]
insert_sort(li)
print(li)

"""
时间复杂度：O(n**2)
优化空间：应用二分法来寻找插入点（然并卵）
"""
