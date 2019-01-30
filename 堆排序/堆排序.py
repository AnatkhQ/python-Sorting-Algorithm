# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/12/9

def sift(li, low, high):
    """
    向下调整函数的实现
    :param li: 列表
    :param low: 堆的根节点位置
    :param high: 堆的最后一个元素的位置
    :return:
    """
    i = low  # i最开始指向根节点
    j = 2 * i + 1  # j开始指向左孩子
    tmp = li[low]  # 把堆顶保存起来，以便向下调整
    while j <= high:  # 只要j位置有数，即小于或等于最后一个元素
        if j + 1 <= high and li[j + 1] > li[j]:  # 如果有右孩子且右孩子>左孩子
            # 用于判断j指向左右哪边
            j = j + 1  # j指向右孩子
        if li[j] > tmp:  # 比堆顶大
            li[i] = li[j]  # 新的堆顶为li[j]
            # 往下看一层，i和j向下移一层
            i = j  # i向下移到j
            j = 2 * i + 1  # j向下移到i的左孩子节点
        else:  # tmp更大，则把tmp放在i位置
            li[i] = tmp  # 把tmp放在某一个领导(非叶子结点)位置上
            break
    else:
        li[i] = tmp  # 如果j>high，把tmp放在叶子节点上

# sift时间复杂度为logn，因为最多走树的高度logn，不是走左边就是走右边
"""
子节点---(n-1)//2--->父节点
列表最后一个元素索引len(n)-1，其中len(n)=n
"""


def heap_sort(li):
    """
    建立一个堆
    (从最后一个非叶子结点进行排序，慢慢扩大范围，直到整个堆)
    :param li:
    :return:
    """
    n = len(li)
    # 最后一个非叶子结点(n-1-1)//2
    for i in range((n - 2) // 2, -1, -1):  # 参数1:range左范围，非叶子结点索引/参数2:range的右范围，即到索引为0的第一个节点，右开特效所以为-1/参数3:步长,倒序为-1
        # i代表建堆时调整的部分根的索引
        sift(li, i, n-1)  # i:根索引=指针low，n-1最后一个元素下标=high指针
    # 建堆完成
    for i in range(n-1, -1, -1):
        # i指向当前堆的最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i-1)  # i-1是新的high


li = list(range(100))
import random
random.shuffle(li)
print(li)
heap_sort(li)
print(li)
"""堆排序的时间复杂度：O(nlogn)"""