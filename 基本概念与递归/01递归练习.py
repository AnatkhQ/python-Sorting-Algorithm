# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/11/19

print("吓得我赶紧", end='')  # end=''取消换行


def func(n):
    if n > 0:
        print("抱着", end='')
        func(n - 1)
        print("得我", end='')
    else:
        print("我的小鲤鱼", end='')


func(3)



'''
    斐波那契
        1,1,2,3,5,8,13,21 从第三个数开始前两个数相加等于当前数
    斐波那契数列的定义:
        f(0) = 1,f(1) = 1,f(n) = f(n-1) + f(n-2)
'''


# 递归:性能不佳，不推荐使用递归
def Fibonacci_Recursion_tool(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci_Recursion_tool(n - 1) + Fibonacci_Recursion_tool(n - 2)


def Fibonacci_Recursion(n):
    result_list = []
    for i in range(1, n + 1):
        result_list.append(Fibonacci_Recursion_tool(i))
    return result_list


# 循环
def Fibonacci_Loop_tool(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1


def Fibonacci_Loop(n):
    result_list = []
    a, b = 0, 1
    while n > 0:
        result_list.append(b)
        a, b = b, a + b
        n -= 1
    return result_list


# yield:性能最好
def Fibonacci_Yield_tool(n):
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, a + b
        n -= 1


def Fibonacci_Yield(n):
    # return [f for i, f in enumerate(Fibonacci_Yield_tool(n))]
    return list(Fibonacci_Yield_tool(n))


'''
题：有n层楼，人可以一次走1步或者2步，问走n层楼有几种走法

解:
    1层楼1种走法
    2层楼2种走法：1,1/2
    3层楼3种走法：1,1,1/1,2/2,1
    4层楼5种走法：1,1,1,1/1,2,1/1,1,2/2,1,1/2,2
    ....
    100层楼
    n层楼：f(n) = f(n-1)+f(n-2)
    
    斐波那契满足条件：
        初项：f(1)=1,f(2)=2
        f(n) = f(n-1)+f(n-2)
'''

'''汉诺塔'''


def hanoi(n, A, B, C):
    if n > 0:
        hanoi(n - 1, A, C, B)
        print("{0}->{1}".format(A, C))
        hanoi(n - 1, B, A, C)


hanoi(3, "A", "B", "C")
'''
次数n | 步数
    2  3
    3  7
    4  15
汉诺塔移动次数的递推式：h(x)=2h(x-1)+1

'''