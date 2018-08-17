# -*- coding:utf-8 -*-
"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）
"""


class Solution:
    # def __init__(self):
    #     self.time = 0
    def __init__(self):
        self.time = [1, 2]

    # def jumpFloor(self, number):
    #     # write code here
    #     if number - 1 > 0:
    #         self.jumpFloor(number - 1)
    #     if number - 2 > 0:
    #         self.jumpFloor(number - 2)
    #     if number - 1 == 0:
    #         self.time += 1
    #     elif number - 2 == 0:
    #         self.time += 1
    #     return self.time
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        if number == 2:
            return 2
        for i in range(2, number + 1):
            self.time.append(self.time[i - 1] + self.time[i - 2])
        return self.time[number]


s = Solution()
print(s.jumpFloor(7))