# -*- coding:utf-8 -*-
"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有
字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵
中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的
某一个格子，则之后不能再次进入这个格子。 例如 a b c e s f c s
a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩
阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一
行第二个格子之后，路径不能再次进入该格子。
"""


class Solution:
    def __init__(self):
        self.b = False

    def hasPath(self, matrix1, rows, cols, path):
        # write code here
        matrix = [[""] * cols for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = matrix1[i * cols + j]
        if not path:
            return True
        if not matrix:
            return False

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == path[0]:
                    self.matchpath(matrix, i, j, [(i, j)], path[1:])
                    if self.b:
                        return True
        return False

    def matchpath(self, matrix, row, col, dict, path):
        if len(path) == 0:
            self.b = True
            return
        if row - 1 >= 0 and matrix[row - 1][col] == path[0] and (row - 1, col) not in dict:
            self.matchpath(matrix, row - 1, col, dict + [(row - 1, col)], path[1:])
        if row + 1 < len(matrix) and matrix[row + 1][col] == path[0] and (row + 1, col) not in dict:
            self.matchpath(matrix, row + 1, col, dict + [(row + 1, col)], path[1:])
        if col - 1 >= 0 and matrix[row][col - 1] == path[0] and (row, col - 1) not in dict:
            self.matchpath(matrix, row, col - 1, dict + [(row, col - 1)], path[1:])
        if col + 1 < len(matrix[0]) and matrix[row][col + 1] == path[0] and (row, col + 1) not in dict:
            self.matchpath(matrix, row, col + 1, dict + [(row, col + 1)], path[1:])


s = Solution()
print(s.hasPath("ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS",5,8,"SLHECCEIDEJFGGFIE"))