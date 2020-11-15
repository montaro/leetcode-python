from typing import List


class Solution:
    def moveZeros(self, nums: List[int]) -> None:
        anchor = 0
        for explore in range(len(nums)):
            if nums[explore] != 0:
                nums[anchor], nums[explore] = nums[explore], nums[anchor]
                anchor = anchor + 1
        return None


if __name__ == '__main__':
    s = Solution()
    nums1 = [0, 1, 0, 3, 12]
    print(nums1)
    s.moveZeros(nums1)
    print(nums1)
    print('-----------------')
    nums2 = [0, 0, 1]
    print(nums2)
    s.moveZeros(nums2)
    print(nums2)
