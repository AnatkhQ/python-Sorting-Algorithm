# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/11/20
''''''
"""
快排
思路：
    取一个元素P（第一个元素），使元素P归位（让p元素，左边比p小，右边比p大）；
    列表被p分成两部分，左边比p小，右边比p大；
    递归完成排序
"""
from 二分查找与Lowb三人组.time_calculate import cal_time

"""
不能给递归函数加装饰器，会导致执行n次装饰器内容，则可对递归函数进行封装优化
"""


def _quick_sort(li, left, right):
    """
    快排
    :param li: 需要排序的列表
    :param left: 左边第一个下标0
    :param right: 右边第一个下标len(li)-1
    :return:
    """
    if left < right:  # left=right一个元素，left>right没有元素
        mid = partition(li, left, right)  # 返回归位元素下标
        # 递归归位元素两侧
        _quick_sort(li, left, mid - 1)  # mid左边
        _quick_sort(li, mid + 1, right)  # mid右边


@cal_time
def quick_sort(li):
    _quick_sort(li, 0, len(li) - 1)


def partition(li, left, right):
    ########最坏情况优化方案#########
    # 原本是找第一个数，li[left]进行从右往左的查找
    i = random.randint(left, right)  # 随机从列表中找一个数的下标
    li[left], li[i] = li[i], li[left]  # 让第一个数li[left]交换成随机选择的数li[i]
    ###############################
    tmp = li[left]  # 拿到左边第一个元素
    while left < right:  # 当游标left<right时一直循环，left=right找到mid
        # 从右边找比tmp小的数，因为左边有空位(把tmp拿出来)，比tmp小的数放在左边
        while left < right and li[right] >= tmp:  # 当右边的数一直大于tmp时，则会一直遍历找到比tmp小的值停止
            #需要添加left<right防止右边的数一直大于左边的数而无法退出循环，当left=right时说明右边全部值大于tmp
            right -= 1  # 往左走一步
        li[left] = li[right]  # 找到右边的值小于tmp的，填写到左边空位
        # 从左边找比tmp大的数，因为右边有空位，比tmp大的数放到右边
        while left < right and li[left] <= tmp:  # 从左边找比tmp大的值
            left += 1
        li[right] = li[left]  # 把左边的值写到右边的空位上
    li[left] = tmp  # 把tmp归位，即跳出大的循环，left=right使左边小于tmp，右边大于tmp
    return left  # 返回mid值，left=right=mid


@cal_time
def sys_sort(li):
    li.sort()


import random
import copy

li = list(range(10000))
random.shuffle(li)  # random.shuffle洗牌，打乱数据顺序
li_sys = copy.deepcopy(li)

quick_sort(li)
sys_sort(li)
print(li)

"""
时间复杂度：O(nlogn) = 有logn层(深度)，每层时间复杂度为n(从左到右，从右到左遍历)
快速排序问题：
    最坏情况:倒序排序 9 8 7 6 5 4 3 2 1 复杂度为n^2
    递归：设置递归深度
        解决的方式是手工设置递归调用深度，方式为：
        import sys   
        sys.setrecursionlimit(1000000) #例如这里设置为一百万
"""
