from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for kid in candies:
            if kid + extraCandies == max(candies):
                result.append(True)
            else:
                result.append(False)
        return result


if __name__ == '__main__':
    print('Hello World!')
