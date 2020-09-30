#Minimum Numbers of Function Calls to Make Target Array

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(bin(x).count('1') for x in nums) + len(bin(max(nums))) - 3