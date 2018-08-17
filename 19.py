# -*- coding:utf-8 -*-
"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12
 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,
 5,6,7,11,10.
"""


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        m = len(matrix)
        n = len(matrix[0])
        out = []
        if n == 1:
            for i in range(m):
                out.append(matrix[i][0])
            return out
        if m == 1:
            for i in range(n):
                out.append(matrix[0][i])
            return out
        dp = [[0] * n for i in range(m)]

        i = 0
        j = 0
        index = 1
        self.recurse(i, j, dp, matrix, out, index)
        return out

    def recurse(self, i, j, dp, matrix, out, index):
        if len(out) == len(matrix) * len(matrix[0]):
            return
        if index == 1:
            for index_j in range(j, len(matrix[0])):
                if dp[i][index_j] == 0:
                    out.append(matrix[i][index_j])
                    dp[i][index_j] = 1
                else:
                    index_j -= 1
                    break
            index = 2
            if dp[i + 1][index_j] == 0:
                self.recurse(i + 1, index_j, dp, matrix, out, index)
            else:
                return
        if index == 2:
            for index_i in range(i, len(matrix)):
                if dp[index_i][j] == 0:
                    out.append(matrix[index_i][j])
                    dp[index_i][j] = 1
                else:
                    index_i -= 1
                    break
            index = 3
            if dp[index_i][j - 1] == 0:
                self.recurse(index_i, j - 1, dp, matrix, out, index)
            else:
                return
        if index == 3:
            for index_j in range(j, -1, -1):
                if dp[i][index_j] == 0:
                    out.append(matrix[i][index_j])
                    dp[i][index_j] = 1
                else:
                    index_j += 1
                    break
            index = 4
            if index_j < len(matrix[0]) and dp[i - 1][index_j] == 0:
                self.recurse(i - 1, index_j, dp, matrix, out, index)
            else:
                return
        if index == 4:
            for index_i in range(i, -1, -1):
                if dp[index_i][j] == 0:
                    out.append(matrix[index_i][j])
                    dp[index_i][j] = 1
                else:
                    index_i += 1
                    break
            index = 1
            if index_i < len(matrix) and dp[index_i][j + 1] == 0:
                self.recurse(index_i, j + 1, dp, matrix, out, index)
            else:
                return


s = Solution()
# print(s.printMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
print(s.printMatrix([[1], [2], [3], [4], [5]]))