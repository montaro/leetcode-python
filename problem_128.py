from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest_consecutive_sequence = 1
        sorted_nums = list(sorted(set(nums)))
        len_nums = len(sorted_nums)
        counter = 1
        for i in range(len_nums):
            n = sorted_nums[i]
            next_n = n + 1
            if i < len_nums - 1 and sorted_nums[i + 1] == next_n:
                counter += 1
                continue
            longest_consecutive_sequence = max(longest_consecutive_sequence, counter)
            counter = 1

        return longest_consecutive_sequence


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
    print(sol.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(sol.longestConsecutive(nums=[]))
