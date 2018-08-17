# -*- coding:utf-8 -*-
"""
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，
总共有多少种方法
i*1 铺i*n
f(n) = f(n-1) + f(n-i)
"""


class Solution:
    def __init__(self):
        self.times = [1, 2]

    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            for i in range(2, number + 1):
                self.times.append(self.times[i - 1] + self.times[i - 2])
        return self.times[number - 1]


s = Solution()
print(s.rectCover(7))