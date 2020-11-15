# Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to
# the right. Note that elements beyond the length of the original array are not written. Do the above modifications
# to the input array in place, do not return anything from your function.


class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                shift_array(arr, i)
                i = i + 1
            i = i + 1


def shift_array(array, start):
    i = len(array) - 1
    while i > start:
        array[i] = array[i - 1]
        i = i - 1
    array[start] = 0
    return array


s = Solution()
a = [1, 0, 2, 3, 0, 4, 5, 0]
s.duplicateZeros(a)
print(a)

# print(shift_array([1, 0, 2, 3, 0, 4, 5, 0], 2))
