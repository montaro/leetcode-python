from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] == arr[j] * 2 and i != j:
                    return True
        return False


s = Solution()
print(s.checkIfExist([10, 2, 5, 3]))
print(s.checkIfExist([-2, 0, 10, -19, 4, 6, -8]))
print(s.checkIfExist([0, 0]))
