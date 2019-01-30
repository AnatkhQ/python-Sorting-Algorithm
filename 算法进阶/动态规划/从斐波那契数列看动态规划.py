# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/12/13

""""""
"""
斐波那契数列列：
练习：使用递归和非递归的方法来求解斐波那契数列的第n项
F n = F n−1 + F n−2
"""

# 子问题的重复计算
def fibnacci(n):
    """
    递归法
    :param n:
    :return:
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fibnacci(n-1) + fibnacci(n-2)




# 动态规划（DP）的思想 = 递推式 + 重复子问题
def fibnacci_no_recurision(n):
    """
    非递归
    :param n:
    :return:
    """
    f = [0,1,1]  # 先确定前2个数为1,1 0的作用是让f[2]=f[0]+f[1]
    if n > 2:
        for i in range(n-2):  # 去掉前两个
            num = f[-1] + f[-2]
            f.append(num)
    return f[n]

print(fibnacci_no_recurision(100))