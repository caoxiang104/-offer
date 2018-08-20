# -*- coding:utf-8 -*-
"""
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
"""


class Solution:
    def multiply(self, A):
        # write code here
        a1 = [1]
        a2= [1]
        temp = 1
        for i in range(len(A)-1):  # A0 -- An-2
            temp *= A[i]
            a1.append(temp)
        temp = 1
        for i in range(len(A)-1, 0, -1):  # An-1 -- A1
            temp *= A[i]
            a2.append(temp)
        b = []
        a2 = a2[::-1]
        for i in range(len(A)):
            b.append(a1[i] * a2[i])
        return b


s = Solution()
print(s.multiply([1, 2, 3, 4, 5]))