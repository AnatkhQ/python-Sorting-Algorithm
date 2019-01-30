# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/12/9

def merge(li, low, mid, high):
    """
    归并的前提：列表分为两段有序
    :param li:
    :param low: 最左指针
    :param mid: 随意的中间值的索引
    :param high: 最右指针
    :return:
    """
    i = low
    j = mid+1
    ltmp = []
    while i<=mid and j<=high:  # 左右两边都有数
        if li[i]<li[j]:  # i指针小于j指针的数
            ltmp.append(li[i])  # 把小的数加到新的列表中
            i+=1
        else:
            ltmp.append(li[j])
            j+=1
    # while执行完，有一部分没值了
    while i<=mid:
        ltmp.append(li[i])
        i+=1
    while j <=high:
        ltmp.append(li[j])
        j += 1
    li[low:high+1] = ltmp  # 新建的列表写回原列表


def merge_sort(li, low, high):
    """
    归并排序
    :param li:
    :param low: 最小值指针
    :param high: 最大值指针
    :return:
    """
    if low<high:  # 至少有两个元素，递归
        mid = (low+high)//2  # mid经过递归，每次都在减半，直到减到1时，跳出进行归并
        merge_sort(li, low, mid)
        merge_sort(li, mid+1, high)
        merge(li, low, mid, high)


li = list(range(1000))
import random
random.shuffle(li)
print(li)
merge_sort(li,0,len(li)-1)
print(li)