#Minimum Operations to Make Array Equal

class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        avg, res = n, 0
        for i in range(0, n):
            if 2 * i + 1 > avg: res += 2 * i + 1 - n
        return res