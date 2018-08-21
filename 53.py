# -*- coding:utf-8 -*-
"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都
表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"
都不是。
"""


class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here\
        index1 = 0  # "."判断指示
        for i in range(len(s)):
            if i == 0 and (s[i] == "+" or s[i] == "-"):  # 第一个字母是否为正负符号
                continue
            elif s[i].isdigit():  # 字母继续
                continue
            elif s[i] == '.':  # 只能出现一次且不能开头
                if index1 == 0:
                    index1 = 1
                    continue
                else:
                    return False
            elif s[i] == "E" or s[i] == "e":
                k = i + 1
                while k < len(s):
                    if k == i + 1 and (s[k] == "-" or s[k] == "+"):
                        if k + 1 < len(s) and s[k + 1].isdigit(): # "-"后面必须带数字
                            k += 1
                        else:
                            return False
                    elif s[k].isdigit():
                        k += 1
                    else:
                        return False
                if s[len(s) - 1] == "E" or s[len(s) - 1] == "e":
                    return False
                break
            else:
                return False
        return True


s = Solution()
print(s.isNumeric("+12.3e+13"))