class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        n = len(A)
        left,right ,s1,s2 = [0]*n, [0]*n,[],[]
        for i,num in enumerate(A):
            count = 1
            while s1 and s1[-1][0] > num:
                count += s1.pop()[1]
            left[i] = count 
            s1.append([num,count])
        for i in range(n)[::-1]:
            count = 1
            while s2 and s2[-1][0] >= A[i]:
                count += s2.pop()[1]
            right[i] = count 
            s2.append([A[i],count])
        return sum(a*l*r for a,l,r in zip(A,left,right))% (10**9 +7)
        
