# -*- coding:utf-8 -*-
"""
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,
你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
"""


class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        max_index = tsum // 2 + 1
        dp = [[0]*(max_index + 1) for i in range(max_index + 1)]
        out = []
        for i in range(1, max_index + 1):
            dp[i][i] = i
        for i in range(1, max_index+1):
            for j in range(i + 1, max_index+1):
                if dp[i - 1][j] != 0:
                    dp[i][j] = dp[i - 1][j] - (i - 1)
                elif dp[i][j - 1] != 0:
                    dp[i][j] = dp[i][j - 1] + j
                if dp[i][j] == tsum:
                    out.append([k for k in range(i, j+1)])
        return out


s = Solution()
print(s.FindContinuousSequence(100))