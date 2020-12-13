from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maxi = max(candies)
        for kid in candies:
            if kid + extraCandies >= maxi:
                result.append(True)
            else:
                result.append(False)
        return result
