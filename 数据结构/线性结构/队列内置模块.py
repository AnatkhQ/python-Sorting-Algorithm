# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/12/10

from collections import deque

q = deque([1,2,3],2)
print(q)  # deque([2, 3], maxlen=2)
q.append(6) # 队尾进队,把2挤掉，3变为队首
print(q.popleft())  # 队首出队:3

# 用于双向队列
q.appendleft(1)  # 队首进队
print(q)  # deque([1, 6], maxlen=2)
q.pop()  # 队尾出队
print(q)  # deque([1], maxlen=2)


def tail(n):
    """
    读取文件后n行
    :param n: 行数
    :return:
    """
    with open('test.txt', 'r') as f:
        q = deque(f, n)
        return q

for line in tail(5):
    print(line, end='')
