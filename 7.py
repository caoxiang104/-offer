# -*- coding:utf-8 -*-
"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出
斐波那契数列的第n项（从0开始，第0项为0）。n<=39
"""


class Solution:
    # def Fibonacci(self, n):
    #     # write code here
    #     if n == 0:
    #         return 0
    #     if n == 1 or n == 2:
    #         return 1
    #     else:
    #         return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
    def __init__(self):
        self.list_ = [0, 1, 1]

    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        else:
            for i in range(3, n+1):
                self.list_.append(self.list_[i - 1] + self.list_[i - 2])
        return self.list_[n]


s = Solution()
print(s.Fibonacci(5))