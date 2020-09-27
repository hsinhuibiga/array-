#Peak Index in a Mountain Array

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) / 2
            if arr[mid - 1] < arr[mid] and arr[mid] < arr[mid + 1]:
                left = mid
            elif arr[mid - 1] > arr[mid] and arr[mid] > arr[mid + 1]:
                right = mid
            else:
                break
        return mid