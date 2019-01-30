# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/12/11

class LinkList:
    class Node:
        def __init__(self, item=None):
            self.item = item
            self.next = None

    class LinkListIterator:  # 迭代器
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:  # 如果node不是空
                cur_node = self.node
                self.node = cur_node.next  # 更新node指向下一个链表
                return cur_node.item  # 返回当前链表存的数据
            else:
                raise StopIteration

        def __iter__(self):
            return self

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        s = LinkList.Node(obj)  # 创建队列
        if not self.head:  # 如果没有队列
            self.head = s  # 把第一个设置为队列
            self.tail = s  # 把第一个设置为尾巴
        else:  # 如果不是空的
            self.tail.next = s  # 接上原本尾巴的next
            self.tail = s  # 获得新的尾巴

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    def __iter__(self):
        return self.LinkListIterator(self.head)  # 创建迭代器

    def __repr__(self):
        # print调用__repr__。map(str, self)把可迭代对象转换成字符串
        return "<<" + ", ".join(map(str, self)) + ">>"  # map(func,iterable)通过函数映射可迭代对象


# 类似于集合的结构
class HashTable:
    def __init__(self, size=101):
        self.size = size  # hash表长度
        self.T = [LinkList() for i in range(self.size)]  # 存放下标的地方

    def h(self, k):
        # hash函数
        return k % self.size

    def insert(self, k):
        i = self.h(k)  # hash值
        if self.find(k):  # 用于去重
            print("Duplicated Insert.")  # 有这个值了
        else:
            self.T[i].append(k)

    def find(self, k):
        i = self.h(k)
        return self.T[i].find(k)


ht = HashTable()

ht.insert(0)
ht.insert(1)
ht.insert(3)
ht.insert(102)
ht.insert(508)

print(",".join(map(str, ht.T)))
print(ht.find(203))
