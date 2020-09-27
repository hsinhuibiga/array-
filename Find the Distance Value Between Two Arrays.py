#Find the Distance Value Between Two Arrays

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        res = 0
        for x in arr1:
            cnt = 0
            for y in arr2:
                if abs(x-y) <= d:
                    break
                else:
                    cnt += 1
                if cnt == len(arr2):
                    res += 1
        return res