# -*- coding:utf-8 -*-
"""
牛客网：剑指offer第二题：
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串
为We%20Are%20Happy。
"""


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        out = []
        for ch in s:
            if ch == " ":
                out.append("%20")
            else:
                out.append(ch)
        return "".join(map(str, out))


s = Solution()
print(s.replaceSpace("Hello World!"))