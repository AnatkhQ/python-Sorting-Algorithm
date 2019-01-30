# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/12/11

class Node:
    """
    创建链表
    """
    def __init__(self, item):
        self.item = item
        self.next = None

def create_linklist_head(li):
    """
    头插法
    :param li:
    :return:
    """
    head =Node(li[0])  # 列表第一个值为头
    for element in li[1:]:  # 列表除了头之外的元素
        node = Node(element)  # 新的链表元素
        node.next = head  # 新的链表插到头部，
        head = node  # 头部为新的链表元素
    return head

def create_linklist_tail(li):
    head = Node(li[0])  # 初始头结点
    tail = head  # 开始尾结点和头结点相同
    for element in li[1:]:
        node = Node(element)
        tail.next = node  # 新的链表插到尾部
        tail = node  # 尾部位新的链表元素
    return head


def print_linklist(lk):
    """
    遍历链表
    :param lk:
    :return:
    """
    while lk:  # 当lk不为None时进行循环
        print(lk.item, end=',')
        lk = lk.next


lk_head = create_linklist_head([1,2,3,6,8,15])
lk_tail = create_linklist_tail([1,2,3,6,8,15])
print_linklist(lk_head)
print_linklist(lk_tail)
