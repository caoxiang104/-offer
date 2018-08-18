# -*- coding:utf-8 -*-
"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能
拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打
印出这三个数字能排成的最小数字为321323。
 * 若ab > ba 则 a > b，
 * 若ab < ba 则 a < b，
 * 若ab = ba 则 a = b；
"""


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        numbers = [str(i) for i in numbers]
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if not self.compare(numbers[i], numbers[j]):
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        return "".join(numbers)

    def compare(self, s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        n = min(n1, n2)
        for i in range(n):
            if s1[i] < s2[i]:
                return True
            elif s1[i] > s2[i]:
                return False
            else:
                continue
        if n2 > n:
            if n2 - n <= n:
                for i in range(n2 - n):
                    if s2[n + i] > s1[i]:   # 12 and 1213
                        return True
                return False  # 12 and 121 or 12 and 1212
            else:
                for i in range(n, n2, n):
                    if s2[i:i+n] > s1:   # 12 and 121312
                        return True
                    elif s2[i:i+n] < s1: # 12 and 121112
                        return False
                    else:
                        continue  # 12 and 121212
                if n2 % n == 0:
                    return True
                else:
                    times = n2 // n
                for i in range(n2 - times*n):
                    if s2[times*n + i] > s1[i]:   # 12 and 1213
                        return True
                return False  # 12 and 121 or 12 and 1212
        elif n1 > n:
            if n1 - n <= n:
                for i in range(n1 - n):
                    if s1[n + i] > s2[i]:   # 1213 and 12
                        return False
                return True  # 121 and 12
            else:
                for i in range(n, n1, n):
                    if s1[i:i+n] > s2:   # 12 and 121312
                        return False
                    elif s1[i:i+n] < s2: # 12 and 121112
                        return True
                    else:
                        continue  # 12 and 121212
                if n1 % n == 0:
                    return True
                else:
                    times = n1 // n
                for i in range(n1 - times*n):
                    if s1[times*n + i] > s2[i]:   # 1213 and 12
                        return False
                return True  # 121 and 12
        else:
            return True


s = Solution()
print(s.PrintMinNumber([3,5,1,4,2]))