# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/12/9

""""""
"""小根堆sift"""
def sift(li, low, high):
    i = low  # i最开始指向根节点
    j = 2 * i + 1  # j开始指向左孩子
    tmp = li[low]  # 把堆顶保存起来，以便向下调整
    while j <= high:  # 只要j位置有数，即小于或等于最后一个元素
        if j + 1 <= high and li[j + 1] < li[j]:  # 如果有右孩子且右孩子<左孩子
            j = j + 1  # j指向右孩子
        if li[j] < tmp:  # 比堆顶小
            li[i] = li[j]  # 新的堆顶为li[j]
            # 往下看一层，i和j向下移一层
            i = j  # i向下移到j
            j = 2 * i + 1  # j向下移到i的左孩子节点
        else:  # tmp更大，则把tmp放在i位置
            li[i] = tmp  # 把tmp放在某一个领导(非叶子结点)位置上
            break
    else:
        li[i] = tmp  # 如果j>high，把tmp放在叶子节点上


def topk(li,k):
    heap = li[0:k]
    for i in range((k-2)//2, -1, -1):
        sift(heap, i, k-1)

    # 1.建堆
    for i in range(k, len(li)-1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k-1)

    # 2.遍历
    for i in range(k-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i-1)

    # 3.出数
    return heap

li = list(range(100))
import random
random.shuffle(li)
print(li)
print(topk(li, 10))


