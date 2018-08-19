# -*- coding:utf-8 -*-
"""
统计一个数字在排序数组中出现的次数。
"""


class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        index = self.find(data, k, 0, len(data) - 1)
        if index == -1:
            return 0
        low = index
        high = index
        while low >= 0:
            if data[low] == k:
                low -= 1
            else:
                break
        while high < len(data):
            if data[high] == k:
                high += 1
            else:
                break
        return high - low - 1

    def find(self, data, value, low, high):
        while low <= high:
            mid = (low + high) // 2
            if data[mid] == value:
                return mid
            elif data[mid] < value:
                high = mid - 1
            else:
                low = mid + 1
        return - 1


s = Solution()
print(s.GetNumberOfK([1, 2, 2, 3, 3, 4], 2))