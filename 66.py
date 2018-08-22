# -*- coding:utf-8 -*-


# class Solution:
#     def movingCount(self, threshold, rows, cols):
#         # write code here
#         self.rows = rows
#         self.cols = cols
#         return self.moving(threshold, 0, 0, [])
#
#     def moving(self, t, i, j, dict_):
#         if self.rows > i >= 0 and self.cols > j >= 0 and (i, j) not in dict_ and self.judge(t, i, j):
#             return 1 + max(self.moving(t, i - 1, j, dict_ + [(i, j)]),
#                            self.moving(t, i + 1, j, dict_ + [(i, j)]),
#                            self.moving(t, i, j - 1, dict_ + [(i, j)]),
#                            self.moving(t, i, j + 1, dict_ + [(i, j)]))
#         else:
#             return 0
#
#     def judge(self, threshold, i, j):
#         return sum(map(int, list(str(i)))) + sum(map(int, list(str(j)))) <= threshold


class Solution:
    def movingCount(self, threshold, rows, cols):
        self.row, self.col = rows, cols
        self.dict = set()
        self.search(threshold, 0, 0)
        return len(self.dict)

    def judge(self, threshold, i, j):
        return sum(map(int, list(str(i)))) + sum(map(int, list(str(j)))) <= threshold

    def search(self, threshold, i, j):
        if not self.judge(threshold, i, j) or (i, j) in self.dict:
            return
        self.dict.add((i, j))
        if i != self.row - 1:
            self.search(threshold, i + 1, j)
        if j != self.col - 1:
            self.search(threshold, i, j + 1)


s = Solution()
print(s.movingCount(5, 10, 10))