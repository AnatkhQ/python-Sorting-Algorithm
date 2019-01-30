# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/12/28

""""""
import random

li = [i for i in range(20)]
random.shuffle(li)
print(li)


def binary_select(li, val):
    """
    二分
    :param li:
    :param val:
    :return:
    """
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] > val:
            right = mid - 1
        elif li[mid] < val:
            left = mid + 1
        else:
            return mid
    else:
        return None


# li_sort = [1, 3, 4, 6, 8, 9, 10]
# binary = binary_select(li_sort, 8)
# print(binary, "在有序的列表中才能使用二分查找法")


def bubble_sort(li):
    """
    冒泡排序
    :param li:
    :return:
    """
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j+1]:
                li[j + 1], li[j] = li[j], li[j + 1]
                exchange = True
        if not exchange:
            return


# bubble_sort(li)
# print(li)


def select_sort(li):
    """
    选择排序
    :param li:
    :return:
    """
    for i in range(len(li)-1):
        min = i
        for j in range(i+1,len(li)):
            if li[min] > li[j]:
                min = j
        li[min], li[i] = li[i], li[min]
        print(li)

# select_sort(li)
# print(li)

def insert_sort(li):
    for i in range(1, len(li)):
        j = i-1
        tmp = li[i]
        while j>=0 and li[j] > tmp:
            li[j+1] = li[j]
            j-=1
        li[j+1] = tmp


insert_sort(li)
print(li)