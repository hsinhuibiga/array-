#Find Lucky Integer in an Array

class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        val = [0] * 501
        for i in arr:
            val[i] += 1
        for inx in range(len(val)-1,0,-1):
            if inx == val[inx]:
                return inx
        return -1