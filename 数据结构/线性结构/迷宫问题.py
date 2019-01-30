# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/12/11

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


def maze_path(x1, x2, y1, y2):
    """
    解决迷宫问题
    :param x1: 起始x
    :param x2: 起始y
    :param y1: 终点x
    :param y2: 终点y
    :return:
    """
    stack = []  # 存放走过的坐标
    stack.append((x1, y1))
    while len(stack) > 0:  # 有坐标能走
        curNode = stack[-1]  # 当前节点
        if curNode[0] == x2 and curNode[1] == y2:
            # 走到终点了
            for p in stack:
                print(p)
            return True

        # x,y四个方向 x+1,y /x-1,y /x,y-1 /x,y+1
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])  # 拿到当前能走的坐标
            # 如果下一个节点能走
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2  # 2表示已经走过的坐标
                break
                # 如果maze[nextNode[0]][nextNode[1]] == 其他值，则直接进入下一循环
        else:
            maze[nextNode[0]][nextNode[1]] = 2
            stack.pop()
    else:
        print("没有路了")
        return False


maze_path(1, 1, 1, 4)
