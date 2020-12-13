from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        length = int(len(nums) / 2)
        l1 = nums[:length]
        l2 = nums[length:]
        for i in range(length):
            result.append(l1[i])
            result.append(l2[i])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.shuffle([1, 2, 3, 4, 5, 6], 3))
