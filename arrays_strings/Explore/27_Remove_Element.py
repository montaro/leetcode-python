class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i = i + 1
        return i


s = Solution()
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
