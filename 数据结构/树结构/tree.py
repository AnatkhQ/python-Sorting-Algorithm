# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/12/11

from collections import deque


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None   # 左孩子
        self.rchild = None # 右孩子

a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e

def pre_order(root):
    """
    前序遍历
    :param root:
    :return:
    """
    if root:  # 是否有root值
        print(root.data, end=',')  # 先打印自己
        pre_order(root.lchild)  # 递归左子树
        pre_order(root.rchild)  # 递归右子树

def in_order(root):
    """
    中序遍历
    :param root:
    :return:
    """
    if root:
        in_order(root.lchild)
        print(root.data, end=',')
        in_order(root.rchild)

def post_order(root):
    """
    后序遍历
    :param root:
    :return:
    """
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=',')

def level_order(root):
    """
    层次遍历
    :param root:
    :return:
    """
    queue = deque()
    queue.append(root)
    while len(queue) > 0: # 只要队不空
        node = queue.popleft()  # 出队
        print(node.data, end=',')
        if node.lchild:  # 如果有左孩子
            queue.append(node.lchild)
        if node.rchild:  # 如果有右孩子
            queue.append(node.rchild)


pre_order(root)

"""
面试题，通过二叉树前序遍历和中序遍历写出二叉树和它的后序遍历
1.前序遍历可以确认第一个元素为根
2.再到中序遍历中找到根的左右两侧子树
3.再通过前序遍历分出左右子树，找到首个左右子树，再重复1、2操作，
检查每一个元素带入中序遍历中，找到左右子树的左边和右边得到对应的子树
4.得到二叉树，写出后序遍历，后序遍历最后一个元素为根元素，每一个子树的根为最后一个元素
左右子树不断划分
"""