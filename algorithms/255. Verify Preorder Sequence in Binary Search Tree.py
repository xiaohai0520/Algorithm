class Solution:          

    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        st = []
        low = float('-inf')
        for x in preorder:
            if x < low:
                return False
            while st and st[-1] < x:
                low = st.pop()
            st.append(x)
        return True

            
