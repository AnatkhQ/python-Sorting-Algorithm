# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/12/10
class Stack(object):
    """栈"""

    def __init__(self):
        self.stack = []

    def is_empty(self):
        """判断是否为空"""
        return self.stack == []

    def push(self, stack):
        """加入元素"""
        self.stack.append(stack)

    def pop(self):
        """弹出元素"""
        return self.stack.pop()

    def get_top(self):
        """返回栈顶元素"""
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        return None

    def size(self):
        """返回栈的大小"""
        return len(self.stack)


def brace_match(s):
    match = {')': '(', ']': '[', '}': '{'}
    stack = Stack()  # 调用栈
    for ch in s:
        if ch in {'(', '[', '{'}:
            stack.push(ch)
        else:  # ch in {')',']','}'}
            if stack.is_empty():
                return False
            elif stack.get_top() == match[ch]:
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False


print(brace_match('[{()}()]{[]}'))







# if __name__ == "__main__":
#     stack = Stack()
#     stack.push("hello")
#     stack.push("world")
#     stack.push("itcast")
#     print(stack.size())
#     print(stack.get_top())
#     print(stack.pop())
#     print(stack.pop())
#     print(stack.pop())
