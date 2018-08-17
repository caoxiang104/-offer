# -*- coding:utf-8 -*-
"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的
后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""


class Solution:
    def reOrderArray(self, array):
        # write code here
        n = len(array)
        list_ = [0] * n
        low = 0
        high = n - 1
        for i in array:
            if i % 2 == 0:
                list_[high] = i
                high -= 1
            else:
                list_[low] = i
                low += 1
        temp = list_[low:]
        list_[low:] = temp[::-1]
        return list_


s = Solution()
print(s.reOrderArray([1, 2, 3, 4, 5, 6]))
