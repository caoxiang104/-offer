# -*- coding:utf-8 -*-
"""
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
"""


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        i = 0
        j = len(array) - 1
        while i != j:
            if array[i] + array[j] == tsum:
                return [array[i], array[j]]
            elif array[i] + array[j] < tsum:
                i += 1
            else:
                j -= 1
        return []


s = Solution()
print(s.FindNumbersWithSum([1, 4, 7, 9, 11, 15], 15))