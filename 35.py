# -*- coding:utf-8 -*-
"""
链接：https://www.nowcoder.com/questionTerminal/96bd6684e04a44eb80e6a68efc0ec6c5
来源：牛客网

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。
即输出P%1000000007
"""


class Solution:
    def __init__(self):
        self.count = 0

    def InversePairs(self, data):
        # write code here
        count = 0
        for i in range(len(data) - 1):
            for j in range(i+1, 0, -1):
                if data[j] < data[i]:
                    count += 1
                    data[j], data[i] = data[i], data[j]
                else:
                    break
                i -= 1
        return count % 1000000007

    def inversePairs1(self, data):
        data = self.merge(data)
        return self.count

    def merge(self, data):
        n = len(data)
        if n == 1:
            return data
        else:
            mid = n // 2
            left = self.merge(data[:mid])
            right = self.merge(data[mid:])
            i = len(left) - 1
            j = len(right) - 1
            k = len(left) + len(right) - 1
            while i >= 0 and j >= 0:
                if left[i] < right[j]:
                    data[k] = right[j]
                    j -= 1
                else:
                    data[k] = left[i]
                    self.count += (j + 1)
                    i -= 1
                k -= 1
            while i >= 0:
                data[k] = left[i]
                i -= 1
                k -= 1
            while j >= 0:
                data[k] = right[j]
                j -= 1
                k -= 1
        return data


s = Solution()
array = [364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,
         648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,
         604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,
         655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
# print(s.InversePairs(array))
print(s.inversePairs1(array))