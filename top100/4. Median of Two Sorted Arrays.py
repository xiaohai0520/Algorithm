class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l=len(nums1)+len(nums2)
        return self.findKth(nums1,nums2,l//2) if l%2==1 else (self.findKth(nums1,nums2,l//2-1)+self.findKth(nums1,nums2,l//2))/2.0

        
        
    def findKth(self,A,B,k):
        if len(A) > len(B):
            A,B = B,A
        if not A:
            return B[k]
        if k == len(A) + len(B) - 1:
            return max(A[-1],B[-1])
        i = len(A) // 2
        j = k - i
        
        if A[i] > B[j]:
            return self.findKth(A[:i],B[j:],i)
        else:
            return self.findKth(A[i:],B[:j],j)
