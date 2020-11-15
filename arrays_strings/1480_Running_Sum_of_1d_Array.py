class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x = 0
        result = []
        for i in nums:
            x = x + i
            result.append(x)
        return result


s = Solution()
print(s.runningSum([1, 2, 3, 4]))
print(s.runningSum([1, 1, 1, 1, 1]))
