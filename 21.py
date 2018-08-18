# -*- coding:utf-8 -*-
"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为
该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的
压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不
可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
"""


class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        for num in pushV:
            if popV:
                if num != popV[0]:
                    stack.append(num)
                else:
                    popV.pop(0)
                    while stack and popV:
                        if stack[-1] == popV[0]:
                            stack.pop()
                            popV.pop(0)
                        else:
                            break
        if popV:
            return False
        else:
            return True


s = Solution()
print(s.IsPopOrder([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))