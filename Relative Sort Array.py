#Relative Sort Array

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        left = []
        right = []
        counter = collections.Counter(arr1)
        for c in arr2:
            if c in arr1 :
                left += [c]*counter[c]
        for c in arr1:
            if c not in arr2 and c not in right:
                right +=[c]*counter[c]
        right.sort()
        return left+right