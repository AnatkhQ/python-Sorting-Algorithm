# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/12/11
from collections import deque

maze = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x, y: (x + 1, y),  # 向上走，x往上移一层
    lambda x, y: (x - 1, y),  # 向下走
    lambda x, y: (x, y - 1),  # 向左
    lambda x, y: (x, y + 1),  # 向右
]


def print_r(path):
    """
    打印走到终点的路径
    :param path:
    :return:
    """
    real_path = []  # 真实路径
    i = len(path) - 1  # 最后一个坐标下标
    while i >= 0:  # 路径里还有值，从终点往前推
        real_path.append(path[i][0:2])  # 添加当前最后一个坐标x，y和上一个路径的下标
        # print(real_path)
        i = path[i][2]  # 拿到上一个路径的下标
    real_path.reverse()  # 路径翻转，从起点走
    for node in real_path:
        print(node)


def maze_path_queue(x1, x2, y1, y2):
    """
    解决迷宫问题
    :param x1: 起始x
    :param x2: 起始y
    :param y1: 终点x
    :param y2: 终点y
    :return:
    """
    queue = deque()
    path = []  # 存储下标，即每个坐标上一个位置的由来，其中第一个数没有由来，自定义为-1
    queue.append((x1, y1, -1))  # 从右边进来，坐标定义为-1
    while len(queue) > 0:  # 队列不空循环
        cur_node = queue.popleft()  # 从左边出去
        path.append(cur_node)
        if cur_node[0] == x2 and cur_node[1] == y2:
            # 到达终点
            print_r(path)
            return True

        for dir in dirs:  # 有几个方向，就同时走几个方向
            next_node = dir(cur_node[0], cur_node[1])
            if maze[next_node[0]][next_node[1]] == 0:
                queue.append((next_node[0], next_node[1], len(path) - 1))
                maze[next_node[0]][next_node[1]] = 2  # 标记为已走过

    return False


maze_path_queue(1, 1, 1, 4)