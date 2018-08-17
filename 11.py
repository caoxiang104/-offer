# -*- coding:utf-8 -*-
"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""


class Solution:
    def NumberOf1(self, n):
        # write code here
        temp_n = n
        list_ = []
        if n >= 0:
            while n != 0:
                list_.append(n%2)
                n = n // 2
            list_ = list_[::-1]
        else:
            n = abs(n)
            while n != 0:
                temp = n % 2
                if temp == 1:
                    list_.append(0)
                else:
                    list_.append(1)
                n = n // 2
            for i in range(len(list_), 32):
                list_.append(1)
            list_ = list_[::-1]
            list_[-1] += 1
            for i in range(len(list_) - 1, 0, -1):
                if list_[i] == 2:
                    list_[i] = 0
                    list_[i - 1] += 1
        if temp_n == -2**31:
            return 1
        else:
            return sum(list_)


s = Solution()
print(s.NumberOf1(-1))