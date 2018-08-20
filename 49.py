# -*- coding:utf-8 -*-
"""
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，
但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的
库函数。 数值为0或者字符串不是一个合法的数值则返回0。
"""


class Solution:
    def StrToInt(self, s):
        # write code here
        index = 1  # 正负号判断
        dic = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "0":0}
        if not s:
            return 0
        out = []
        for i in range(len(s)):
            if s[i] == " ":
                continue
            elif s[i] == "+" and not out:
                index = 1
            elif s[i] == "-" and not out:
                index = -1
            elif s[i] in dic.keys():
                out.append(dic[s[i]])
            else:
                return 0
        num = 0
        n = len(out)
        for i in range(n):
            num += (out[i] * 10**(n - 1 - i))
        return index*num


s = Solution()
print(s.StrToInt("  -12  3"))