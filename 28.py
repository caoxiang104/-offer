# -*- coding:utf-8 -*-
"""
数组中有一个数字出现的次数超过数组长度的一半，
请找出这个数字。例如输入一个长度为9的数组{1,
2,3,2,2,2,5,4,2}。由于数字2在数组中出现了
5次，超过数组长度的一半，因此输出2。如果不
存在则输出0。
"""


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        s = set(numbers)
        max_sum = 0
        max_num = 0
        for i in s:
            if numbers.count(i) > max_sum:
                max_sum = numbers.count(i)
                max_num = i
        if max_sum > len(numbers) // 2:
            return max_num
        else:
            return 0


s = Solution()
print(s.MoreThanHalfNum_Solution([1, 2, 2, 3]))