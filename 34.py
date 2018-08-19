# -*- coding:utf-8 -*-
"""
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到
第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1
（需要区分大小写）.
"""


class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i+1
        return 0


s = Solution()
print(s.FirstNotRepeatingChar([1, 2, 1, 2, 3, 4, 5]))