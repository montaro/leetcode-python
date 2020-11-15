class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = {}
        result = []
        for i in nums:
            if i in m:
                m[i] = m[i] + 1
            else:
                m[i] = 1
        for k, v in m.items():
            if v > 1:
                result.append(k)
        return result


s = Solution()
print(s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
