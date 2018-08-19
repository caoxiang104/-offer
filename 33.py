# -*- coding:utf-8 -*-
"""
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的
顺序的第N个丑数。
"""


class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        list_ = []
        for i in range(30):
            for j in range(20):
                for k in range(15):
                    list_.append(2 ** i * 3 ** j * 5 ** k)
        list_.sort()
        return list_[index - 1] if index else 0


s = Solution()
print(s.GetUglyNumber_Solution(500))