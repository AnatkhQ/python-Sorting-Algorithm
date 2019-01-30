# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/12/12

""""""
"""
LEGB 分别是:

locals 是函数内的名字空间，包括局部变量和形参
enclosing 外部嵌套函数的名字空间（闭包中常见）
globals 全局变量，函数定义所在模块的名字空间
builtins 内置模块的名字空间
而查找的优先顺序从左到右以此是: L -> E -> G -> B
"""
# 题目1
# l = []
# for i in range(1, 10):
#     f = lambda x: x * i
#     l.append(f)
#     # print(f(1),id(i),id(f(1)))
#
# print('i',i)  # 循环里的i是全局变量，循环完之后i=9
# for f in l:
#     print(f(1),id(f(1)))


# 题目2
# l = []
#
# for i in range(10):
#     def x(n):  # 函数的形参属于函数内部名称空间，属于局部，所以n为123456789
#         print(n)
#         return lambda p: p * n
#     l.append(x(i))
#
# for f in l:
#     print(f(1))


#题目3
l = []

for i in range(10):
    def x():
        return lambda p: p * i
    l.append(x())

for f in l:
    print(f(1))

# 块级作用域

# if 1 == 1:
#     name = "lzl"
#
# print(name)
#
# for i in range(10):
#     age = i
#
# print(age)


# 终极版作用域

    # name = "lzl"
    #
    #
    # def f1():
    #     print(name)
    #
    #
    # def f2():
    #     name = "eric"
    #     return f1
    #
    #
    # ret = f2()
    # print(id(ret)==id(f1))  # True
    # print(ret is f1)  # True
    # ret()

# 输出：lzl



# 终极版作用域

# name = "lzl"
#
#
# def f1():
#     print(name)
#
#
# def f2():
#     name = "eric"
#     f1()

# 在函数未执行之前，作用域已经形成了，作用域链也生成了
# f2()
# print(f2() is f1())  # lzl lzl True


# li = [lambda :x for x in range(10)]
# print(type(li))  # list
# print(type(li[0]))  # func
#
# print(id(li[0]))  # 函数内存地址不同
# print(id(li[1]))  # 函数内存地址不同
#
# print(id(li[0]()))  # 返回值指向同一个地址
# print(id(li[1]()))
# print(id(li[2]()))
#
# res = li[0]()
# print(res)
"""li第一个函数的返回值为9还不是0，记住：函数在没有执行前，内部代码不执行"""
# <class 'list'>
# <class 'function'>