# -*- coding:utf-8 -*-
"""
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
"""


class Solution:
    def Sum_Solution(self, n):
        # write code here
        sum_ = n
        return sum_ > 0 and (sum_ + self.Sum_Solution(n - 1))


s = Solution()
print(s.Sum_Solution(3))
