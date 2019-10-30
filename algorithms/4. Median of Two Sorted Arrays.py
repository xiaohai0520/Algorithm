#use find kth
# get half of A and k-part(A) from B if A > B ,to find i
#if B > A, to find j

# 1. 我们可以先讲两个数组合并，然后进行排序。如果是奇数个，取中间的一位，如果是偶数个，取中间两位求平均值。时间复杂度O((m+n)log(m+n))
# 2. 由于两个数组都是已经排好序的，我们可以用递归的方法去找到第K个。
# 每次取较短的数组的一半，i = 长度 / 2, j = k - i, 对比第一个数组中的第i位和第二个数组中的第j位，
# 如果第一个数组中的数大，说明第二个数组的前j个数是一定存在于前K，然后只要在A的前i个和B的后j个数中找出第i大的数就可以了。
# 反之也是一样，一直递归下去，知道小的数组没有或者k为两个数组长度之和。时间复杂度O(log(m+n))。

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l=len(nums1)+len(nums2)
        return self.findKth(nums1,nums2,l//2) if l%2==1 else (self.findKth(nums1,nums2,l//2-1)+self.findKth(nums1,nums2,l//2))/2.0


    def findKth(self,A,B,k):
        if len(A)>len(B):
            A,B=B,A
        if not A:
            return B[k]
        if k==len(A)+len(B)-1:
            return max(A[-1],B[-1])
        i=len(A)//2
        j=k-i
        if A[i]>B[j]:
            return self.findKth(A[:i],B[j:],i)
        else:
            return self.findKth(A[i:],B[:j],j)
