# -*- coding:utf-8 -*-
"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的
所有字符串abc,acb,bac,bca,cab和cba。
"""


class Solution:
    def __init__(self):
        self.out = []

    def Permutation(self, ss):
        # write code here
        if len(ss) == 1:
            return ss
        self.out = list(set(self.recurse(ss)))
        return sorted(self.out)

    def recurse(self, ss, string=""):
        if len(ss) == 1:
            self.out.append(string+ss[0])
        for i in range(len(ss)):
            if i == 0:
                self.recurse(ss[i+1:], string+ss[i])
            elif i == len(ss) - 1:
                self.recurse(ss[:-1], string+ss[i])
            else:
                self.recurse(ss[:i]+ss[i+1:], string+ss[i])
        return self.out


s = Solution()
print(s.Permutation("aab"))