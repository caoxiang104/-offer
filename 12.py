# -*- coding:utf-8 -*-
"""
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方
"""


class Solution:
    def Power1(self, base, exponent):
        # write code here
        return base ** exponent

    def Power(self, base, exponent):

        def recurse(base, exponent):
            if exponent == 1:
                return base
            else:
                if exponent % 2 == 0:
                    return recurse(base, exponent // 2) * recurse(base, exponent // 2)
                else:
                    return recurse(base, (exponent - 1) // 2) * recurse(base, (exponent - 1) // 2) * base

        if base == 0:
            return 0
        elif exponent > 0 and exponent % 2 == 0:
            return recurse(base, exponent)
        elif exponent > 0 and exponent % 2 != 0:
            return recurse(base, exponent - 1) * base
        elif exponent < 0 and abs(exponent) % 2 == 0:
            return 1/recurse(base, abs(exponent))
        elif exponent < 0 and abs(exponent) % 2 != 0:
            return 1/(recurse(base, abs(exponent) - 1) * base)
        elif exponent == 0:
            return 1


s = Solution()
print(s.Power(2, 0))
print(s.Power1(2, 0))