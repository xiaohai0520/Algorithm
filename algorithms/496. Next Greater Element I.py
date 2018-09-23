#use stack and dic to save the next larger one


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # res = []
        # for num in nums1:
        #     index = nums2.index(num)
        #     for i in range(index,len(nums2)):
        #         if nums2[i] > num:
        #             res.append(nums2[i])
        #             break
        #         elif i == len(nums2) - 1:
        #             res.append(-1)
        # return res
        d = {}
        st = []
        ans = []
        
        for x in nums2:
            while len(st) and st[-1] < x:
                d[st.pop()] = x
            st.append(x)

        for x in nums1:
            ans.append(d.get(x, -1))
            
        return ans
