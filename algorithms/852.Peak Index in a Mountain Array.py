class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l,r = 0,len(A) -1 

        while l < r:
            mid = (l + r)//2
            if A[mid] > A[mid + 1]:
                r = mid + 1
            else:
                l = mid + 1
        
        return l       
