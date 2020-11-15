class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        window = False
        ones = []
        for i in nums:
            if i == 1:
                if not window:
                    window = True
                    ones.append(1)
                else:
                    ones[-1] = ones[-1] + 1
                # new window of ones starts
            else:
                window = False
        if len(ones) == 0:
            return 0
        return max(ones)


s = Solution()
print(s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
