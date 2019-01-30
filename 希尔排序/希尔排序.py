# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/12/10

""""""
"""
希尔排序(Shell Sort)是一种分组插入排序算法(插入算法升级版)
"""


# def shell_sort(alist):
#     n = len(alist)
#     # 初始步长
#     gap = n//2
#     while gap > 0:
#         # 按步长进行插入排序
#         for i in range(gap, n):  # gap为分组后，第一个抽到的牌
#             j = i
#             # 插入排序
#             while j>=gap and alist[j-gap] > alist[j]:
#                 alist[j-gap], alist[j] = alist[j], alist[j-gap]
#                 j -= gap
#         # 得到新的步长
#         gap = gap // 2
#
# alist = [54,26,93,17,77,31,44,55,20]
# shell_sort(alist)
# print(alist)

def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):  # i表示摸到的牌的下标
        tmp = li[i]
        j = i - gap  # j指的是手里的牌的下标
        while j >= 0 and li[j] > tmp:
            li[j + gap] = li[j]  # 摸到的牌和手上的牌的值进行替换
            j -= gap  # 这组的下一个值
        li[j + gap] = tmp  # 不进行交换，保留摸到的牌原本的值


def shell_sort(li):
    d = len(li) // 2  # 进行分组
    while d >= 1:  # 分组结束条件为分组=1，
        insert_sort_gap(li, d)  # 调用插入排序
        d //= 2  # 得到新的分组步长

alist = [54,26,93,17,77,31,44,55,20]
shell_sort(alist)
print(alist)