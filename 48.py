# -*- coding:utf-8 -*-
"""
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
"""


class Solution:
    def Add(self, num1, num2):
        # write code here
        if num1 == 0:
            return num2
        elif num2 == 0:
            return num1
        elif num1 > 0 and num2 > 0:    # 大的前，小的后
            if num1 > num2:
                sum_ = self.binAdd(bin(num1)[2:], bin(num2)[2:])
            else:
                sum_ = self.binAdd(bin(num2)[2:], bin(num1)[2:])
            sum_ = int("".join(sum_), 2)
        elif num1 < 0 and num2 < 0:
            if abs(num1) > abs(num2):
                sum_ = self.binAdd(bin(num1)[3:], bin(num2)[3:])
            else:
                sum_ = self.binAdd(bin(num2)[3:], bin(num1)[3:])
            sum_ = -int("".join(sum_), 2)
        elif num1 > 0:
            index = -1    # -1 表示减法
            if num1 > abs(num2):
                sum_ = self.binAdd(bin(num1)[2:], bin(num2)[3:], index)
                sum_ = int("".join(sum_), 2)
            else:
                sum_ = self.binAdd(bin(num2)[3:], bin(num1)[2:], index)
                sum_ = -int("".join(sum_), 2)
        else:
            index = -1
            if num2 > abs(num1):
                sum_ = self.binAdd(bin(num2)[2:], bin(num1)[3:], index)
                sum_ = int("".join(sum_), 2)
            else:
                sum_ = self.binAdd(bin(num1)[3:], bin(num2)[2:], index)
                sum_ = -int("".join(sum_), 2)
        return sum_

    def binAdd(self, num1, num2, index=1):
        out = []
        n = len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        temp_index = 0
        if index > 0:
            for i in range(n):
                if num1[i] == '1' and num2[i] == '1':
                    if temp_index == 0:
                        out.append('0')
                    else:
                        out.append('1')
                    temp_index = 1
                elif num1[i] == '0' and num2[i] == '0':
                    if temp_index == 0:
                        out.append('0')
                    else:
                        out.append('1')
                    temp_index = 0
                else:
                    if temp_index == 0:
                        out.append('1')
                        # temp_index = 0
                    else:
                        out.append('0')
                        # temp_index = 1
            for i in range(n, len(num1)):  # 多余部分
                if temp_index == 1:
                    if num1[i] == '0':
                        out.append('1')
                        temp_index = 0
                    else:
                        out.append('0')
                        temp_index = 1
                else:
                    out.append(num1[i])
            if temp_index == 1:
                out.append('1')
        else:
            for i in range(n):
                if (num1[i] == '1' and num2[i] == '1') or (num1[i] == '0' and num2[i] == '0'):
                    if temp_index == 0:
                        out.append('0')
                        # temp_index = 0
                    else:
                        out.append('1')
                        # temp_index = 1
                elif num1[i] == '1' and num2[i] == '0':
                    if temp_index == 0:
                        out.append('1')
                    else:
                        out.append('0')
                    temp_index = 0
                else:
                    if temp_index == 0:
                        out.append('1')
                    else:
                        out.append('0')
                    temp_index = 1
            for i in range(n, len(num1)):
                if temp_index == 1:
                    if num1[i] == '0':
                        out.append('1')
                        temp_index = 1
                    else:
                        out.append('0')
                        temp_index = 0
                else:
                    out.append(num1[i])
        return out[::-1]

    def add(self, num1, num2):
        while num2 != 0:
            num1, num2 = (num1 ^ num2), ((num1 & num2) << 1)
            num1 &= 0xFFFFFFFF
            num2 &= 0xFFFFFFFF
            if num1 > 0x7FFFFFFF:
                num1 = ~(num1 ^ 0xFFFFFFFF)  # 补运算符
        return num1


s = Solution()
print(s.Add(-5, -6))
print(s.add(-5, -6))