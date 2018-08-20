class Solution:
    def IsContinuous(self, numbers):
        # write code here
        sorted(numbers)
        que = 0
        for i in range(len(numbers)):
            if numbers[i] == 0:
                que += 1
            else:
                if numbers[i] == numbers[i - 1] + 1 or que == i:
                    continue
                else:
                    if que > 0:
                        que -= 1
                    else:
                        return "false"
        return "true"


s = Solution()
print(s.IsContinuous([1, 3, 2, 6, 4]))