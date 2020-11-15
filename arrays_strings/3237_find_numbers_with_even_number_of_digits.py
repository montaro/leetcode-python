# Given an array nums of integers, return how many of them contain an even number of digits.


def count_digits(number):
    """
    :type number: int
    :rtype: int
    """
    if number == 0:
        return 1
    result = 0
    while number != 0:
        result = result + 1
        number = int(number / 10)
    return result


class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in nums:
            if count_digits(i) % 2 == 0:
                result = result + 1
        return result


s = Solution()
print(count_digits(23))
print(s.findNumbers([12, 345, 2, 6, 7896]))
