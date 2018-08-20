# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if not s and not pattern:
            return True
        if not pattern:
            return False
        if not s:   # s不存在 a*, b**都可以消去
            for i in range(len(pattern) - 1):
                if pattern[i] != "*" and pattern[i + 1] != "*":
                    return False
            if pattern[len(pattern) - 1] != "*":  # 最后一个为字母不可消除
                return False
            return True
        i = 0
        j = 0
        while i < len(s) and j < len(pattern):
            if s[i] == pattern[j]:
                i += 1
                j += 1
            else:
                if pattern[j] == "*":   # 考虑为*的情况
                    if j == 0:  # 第一个不能为*
                        return False
                    elif j > 0 and pattern[j - 1] != s[i] and pattern[j - 1] != ".":   # 不能用前一个补的情况
                        if j + 1 < len(pattern) - 1 and i - 1 >= 0 and pattern[j + 1] == s[i - 1]:
                            # 把前一个消去  如 cb 和 c*cb
                            if j + 2 < len(pattern) - 1 and pattern[j + 2] == s[i]:
                                # 可以消去
                                j += 3
                            else:
                                # 不可消去
                                return False
                        elif j + 1 < len(pattern) - 1 and pattern[j + 1] == s[i]:
                            # 把*作废
                            j += 2
                        else:
                            return False
                    elif j > 0 and (pattern[j - 1] == s[i] or pattern[j - 1] == "."):
                        # 能用前一个补的情况
                        times_i = 1
                        times_j = 0
                        while i + 1 < len(s) and s[i + 1] == s[i]:
                            # 把所有的与s[i]等的 如 aaaa
                            times_i += 1
                            i += 1
                        while j + 1 < len(pattern) and pattern[j + 1] == s[i]:
                            # 把所有的与s[i] 如 a*aa
                            times_j += 1
                            j += 1
                        if j + 1 < len(pattern) and pattern[j + 1] == "*":
                            # 把所有的与s[i] 如 a*aa*
                            j += 1
                            times_j -= 1
                            while j + 1 < len(pattern) and pattern[j + 1] == s[i]:
                                # 把所有的与s[i] 如 a*aa*a
                                times_j += 1
                                j += 1
                        if j + 2 < len(pattern) and pattern[j + 2] == '*':
                            # 把所有的与s[i] 如 a*aac*
                            j += 2
                            while j + 1 < len(pattern) and pattern[j + 1] == s[i]:
                                # 把所有的与s[i] 如 a*aac*aa
                                times_j += 1
                                j += 1
                        if times_j <= times_i + 1:
                            j += 1
                            i += 1
                        else:
                            return False
                elif pattern[j] == ".":
                    i += 1
                    j += 1
                elif j + 1 < len(pattern) and pattern[j + 1] == "*":
                    # 后一个为*
                    j += 2
                else:
                    return False
        if i == len(s) and j == len(pattern):
            return True
        else:
            if j != len(pattern):
                for k in range(j, len(pattern) - 1):
                    if pattern[k] != "*" and pattern[k + 1] != "*":
                        return False
                if pattern[len(pattern) - 1] != "*":
                    return False
                else:
                    return True
            else:
                return False


s = Solution()
print(s.match("bbbba", ".*a*a"))