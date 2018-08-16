# -*- coding:utf-8 -*-
"""
牛客网：剑指offer第一题：
在一个二维数组中（每个一维数组的长度相同），每一行都
按照从左到右递增的顺序排序，每一列都按照从上到下递增
的顺序排序。请完成一个函数，输入这样的一个二维数组和
一个整数，判断数组中是否含有该整数。
"""


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        m = len(array)
        n = len(array[0])
        dp = [[0]*n for i in range(m)]
        if m == 0 or n == 0:
            return False

        def recurse(dp, array, index_i, index_j):
            dp[index_i][index_j] = 1
            index1 = 0
            index2 = 0
            if array[index_i][index_j] == target:
                return True
            elif array[index_i][index_j] > target:
                if index_i - 1 >= 0 and dp[index_i - 1][index_j] == 0:
                    index1 = recurse(dp, array, index_i - 1, index_j)
                if index_j - 1 >= 0 and dp[index_i][index_j - 1] == 0:
                    index2 = recurse(dp, array, index_i, index_j - 1)
                if index1 == 1 or index2 == 1:
                    return True
            else:
                if index_i + 1 <= m - 1 and dp[index_i + 1][index_j] == 0:
                    index1 = recurse(dp, array, index_i + 1, index_j)
                if index_j + 1 <= n - 1 and dp[index_i][index_j + 1] == 0:
                    index2 = recurse(dp, array, index_i, index_j + 1)
                if index1 == 1 or index2 == 1:
                    return True
            return False
        index = recurse(dp, array, 0, 0)
        return index


s = Solution()
print(s.Find(7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))