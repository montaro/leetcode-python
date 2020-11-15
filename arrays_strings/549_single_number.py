from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
        for k in d:
            if d[k] == 1:
                return k
        return None


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([2, 2, 1]))
    print(s.singleNumber([4, 1, 2, 1, 2]))
    print(s.singleNumber([1]))
