# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/11/20
''''''
'''
冒泡排序，长度为n的列表，走n-1趟
每走一趟，把无序区最大的数放在最后，即冒泡，并把无序区的其他比较大的数，稍微往上移了一些
指针走到n-1停下，因为n为冒泡的数，之后重新回到无序区0的位置
走i趟，则指针在n-1-i(-1:指针每次都少走一位，因为n为要冒泡的值;-i:第i趟，就已经有i个冒泡的值)
'''
from 二分查找与Lowb三人组.time_calculate import cal_time

@cal_time
def bubble_sort(li):
    for i in range(0, len(li) - 1):
        # i表示第i趟 有序区有i个数
        for j in range(0, len(li) - i - 1):  # 循环无序区
            if li[j] > li[j + 1]:  # 如果指针j大于j+1，则需要移动位置
                li[j], li[j + 1] = li[j + 1], li[j]  # 当前位置j替换成j+1，j+1替换成j


@cal_time
def bubble_sort_plus(li):
    for i in range(len(li) - 1):
        # i表示第i趟 有序区有i个数
        exchange = False  # 标识符为False
        for j in range(len(li) - i - 1):  # 循环无序区
            if li[j] > li[j + 1]:  # 如果指针j大于j+1，则需要移动位置
                li[j], li[j + 1] = li[j + 1], li[j]  # 当前位置j替换成j+1，j+1替换成j
                exchange = True  # 如果有交换位置则改为True

        if not exchange:  # 如果走完一趟，依然为False
            return  # 则说明这一趟不改变顺序，为有序，减少循环次数
        print(li)

import random

li = [2,5,4,8,7,6,9,1,3]
# random.shuffle(li)  # random.shuffle洗牌，打乱数据顺序
# bubble_sort(li)
bubble_sort_plus(li)
print(li)
'''
总结：冒泡排序时间复杂度O(n**2)速度太慢
     如果冒泡执行一趟没有进行交换，则已经是排好序的列表，直接结束算法
'''