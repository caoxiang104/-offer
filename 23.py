# -*- coding:utf-8 -*-
"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结
果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        left = []
        right = []
        if not sequence:
            return False
        temp = sequence[-1]
        for i in range(len(sequence) - 1):
            if sequence[i] < temp:
                left.append(sequence[i])
            else:
                right.append(sequence[i])
        if left and right:
            if sequence.index(left[len(left) - 1]) > sequence.index(right[0]):
                return False
            else:
                temp1 = self.VerifySquenceOfBST(left)
                if not temp1:
                    return False
                temp2 = self.VerifySquenceOfBST(right)
                if not temp2:
                    return False
        elif left or right:
            if left:
                temp1 = self.VerifySquenceOfBST(left)
                if not temp1:
                    return False
            if right:
                temp2 = self.VerifySquenceOfBST(right)
                if not temp2:
                    return False
        return True


s = Solution()
print(s.VerifySquenceOfBST([1, 2, 5, 7, 3, 4]))