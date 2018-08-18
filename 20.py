# -*- coding:utf-8 -*-
"""
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
"""


class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        # write code here
        if not self.minStack:
            self.minStack.append(node)
        else:
            if node < self.minStack[-1]:
                self.minStack.append(node)
            else:
                self.minStack.append(self.minStack[-1])
        self.stack.append(node)

    def pop(self):
        # write code here
        if self.stack:
            self.minStack.pop()
            return self.stack.pop()

    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]

    def min(self):
        # write code here
        if self.minStack:
            return self.minStack[-1]


s = Solution()
s.push(3)
print(s.min())
s.push(4)
print(s.min())
s.push(2)
print(s.min())
s.pop()
print(s.min())
print(s.top())
print(s.top())