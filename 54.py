# -*- coding:utf-8 -*-
"""
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只
出现一次的字符是"g"。当从该字符流中读出前六个字符
“google"时，第一个只出现一次的字符是"l"。
"""


class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ""

    def FirstAppearingOnce(self):
        # write code here
        set_ = set(self.s)
        dic = dict()
        for i in set_:
            dic[i] = self.s.count(i)
        for i in self.s:
            if dic[i] == 1:
                return i
        return "#"

    def Insert(self, char):
        # write code here
        self.s += char


s = Solution()
s.Insert("asdfffa")
print(s.FirstAppearingOnce())